from __future__ import annotations

from typing import Any
from urllib.parse import parse_qs

import curl_cffi.requests
from curl_cffi.requests import AsyncSession

from FireBased.client.proto import CheckInRequestMessage, CheckInResponseMessage
from FireBased.client.schemas import FirebaseInstallationRequestResponse, RegisterInstallRequestBody, RegisterGcmRequestBody, RegisterGcmRequestResponse
from FireBased.client.settings import FireBasedSettings


class FireBasedClient:
    """API wrapper for interaction with the Google Firebase API"""

    def __init__(
            self,
            curl_cffi_kwargs: dict[str, Any] = None,
            curl_cffi_client: curl_cffi.requests.AsyncSession = None
    ):
        # Ensure that the client is not supplied when kwargs are supplied & vice versa
        assert not (curl_cffi_kwargs and curl_cffi_client), "Cannot supply both initialization kwargs and a client"

        self._http_session_external: AsyncSession | None = curl_cffi_client
        self._http_session: AsyncSession | None = curl_cffi_client or None
        self._http_session_kwargs: dict[str, Any] = curl_cffi_kwargs

    async def __aenter__(self) -> FireBasedClient:
        """
        Enter the context manager & create the HTTP client

        :return: The HTTP client instance

        """

        # Supply the client when entering the context manager
        self._http_session = self._http_session_external or curl_cffi.requests.AsyncSession(
            verify=False,
            ja3=self._http_session_kwargs.pop('ja3', FireBasedSettings.http_client_ja3),
            **(self._http_session_kwargs or dict())
        )

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Close the HTTP client when exiting the context manager"""

        if not self._http_session_external:
            await self._http_session.close()

        self._http_session = None

    async def check_in(
            self,
            body: CheckInRequestMessage
    ) -> CheckInResponseMessage:
        """
        Complete the Firebase Google Checkin

        :param body: The checkin request body
        :return: The checkin response

        """

        httpx_response: curl_cffi.requests.Response = await self._http_session.post(
            url=FireBasedSettings.check_in_url,
            headers=FireBasedSettings.check_in_headers,
            data=bytes(body)
        )

        return CheckInResponseMessage().parse(httpx_response.content)

    async def register_install(
            self,
            body: RegisterInstallRequestBody
    ) -> FirebaseInstallationRequestResponse:
        """
        Register the installation of an app with Firebase

        :param body: The installation request body
        :return: The installation response

        """

        included_headers: dict = {
            "user-agent": body.user_agent,
            'x-goog-api-key': body.app_public_key,
            'x-android-package': body.app_package,
            'x-android-cert': body.app_cert,
            **FireBasedSettings.register_install_headers
        }

        httpx_response: curl_cffi.requests.Response = await self._http_session.post(
            url=FireBasedSettings.register_install_url.format(appName=body.app_name),
            headers=included_headers,
            json=body.json_body.model_dump()
        )

        return FirebaseInstallationRequestResponse(**httpx_response.json())

    async def register_gcm(
            self,
            body: RegisterGcmRequestBody
    ) -> RegisterGcmRequestResponse:
        """
        Register the GCM token with Firebase

        :param body:  The GCM registration request body
        :return: The GCM registration response

        """

        included_headers: dict = {
            "Authorization": f"AidLogin {body.android_id}:{body.security_token}",
            "User-Agent": body.user_agent
        }

        httpx_response: curl_cffi.requests.Response = await self._http_session.post(
            url=FireBasedSettings.register_gcm_url,
            headers=included_headers,

            # Must be data so that it uses the aliases when encoding to JSON
            data=body.json_body.model_dump(by_alias=True)
        )

        # Parse the response & return it
        return RegisterGcmRequestResponse(**{k.lower(): v for k, v in parse_qs(httpx_response.text).items()})
