from typing import Any
from urllib.parse import parse_qs

import curl_cffi.requests

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
        curl_cffi_kwargs = curl_cffi_kwargs or dict()
        self._provided_client: bool = bool(curl_cffi_client)
        self._http_client = curl_cffi_client or curl_cffi.requests.AsyncSession(
            verify=False,
            ja3=curl_cffi_kwargs.pop('ja3', FireBasedSettings.http_client_ja3),
            **(curl_cffi_kwargs or dict())
        )

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if not self._provided_client:
            await self._http_client.close()

    @property
    def client(self) -> curl_cffi.requests.AsyncSession:
        """HTTP Client instance"""
        return self._http_client

    async def check_in(
            self,
            body: CheckInRequestMessage,
            **kwargs
    ) -> CheckInResponseMessage:
        """Complete check-in with Android & return response"""

        httpx_response: curl_cffi.requests.Response = await self._http_client.post(
            url=FireBasedSettings.check_in_url,
            headers={**FireBasedSettings.check_in_headers, **kwargs.pop('headers', {})},
            data=bytes(body),
            **kwargs
        )

        return CheckInResponseMessage().parse(httpx_response.content)

    async def register_install(
            self,
            body: RegisterInstallRequestBody,
            **kwargs
    ) -> FirebaseInstallationRequestResponse:
        """Register the installation with Firebase"""

        # Create headers
        headers: dict = {
            "user-agent": body.user_agent,
            **FireBasedSettings.register_install_headers,
            **kwargs.pop('headers', {}),
            'x-goog-api-key': body.app_public_key,
            'x-android-package': body.app_package,
            'x-android-cert': body.app_cert
        }

        # Send request
        httpx_response: curl_cffi.requests.Response = await self._http_client.post(
            url=FireBasedSettings.register_install_url.format(appName=body.app_name),
            headers=headers,
            json=body.json_body.model_dump(),
            **kwargs
        )

        return FirebaseInstallationRequestResponse(**httpx_response.json())

    async def register_gcm(
            self,
            body: RegisterGcmRequestBody,
            **kwargs
    ) -> RegisterGcmRequestResponse:
        headers: dict = {
            "Authorization": f"AidLogin {body.android_id}:{body.security_token}",
            "User-Agent": body.user_agent,
            **kwargs.pop('headers', {})
        }

        httpx_response: curl_cffi.requests.Response = await self._http_client.post(
            url=FireBasedSettings.register_gcm_url,
            headers=headers,
            data=body.json_body.model_dump(by_alias=True),  # Must be data so that it uses the aliases when encoding to JSON
            **kwargs
        )

        parsed_data = parse_qs(httpx_response.text)
        return RegisterGcmRequestResponse(**{key.lower(): value[0] for key, value in parsed_data.items()})
