import random
import string

from pydantic import BaseModel, Field

from FireBased.client.proto import CheckInResponseMessage


def generate_firebase_id() -> str:
    """Generates a dummy Firebase ID (fid)"""

    char_pool = string.ascii_letters + string.digits
    firebase_id = ''.join(random.choices(char_pool, k=22))
    hyphen_pos = random.randint(1, 20)
    return firebase_id[:hyphen_pos] + '-' + firebase_id[hyphen_pos:]


class RegisterInstallRequestBodyJsonBody(BaseModel):
    appId: str
    fid: str = Field(default_factory=generate_firebase_id)
    authVersion: str = "FIS_v2"
    sdkVersion: str = "a:17.2.0"


class FirebaseInstallationRequestResponseAuthToken(BaseModel):
    token: str
    expiresIn: str


class FirebaseInstallationRequestResponse(BaseModel):
    authToken: FirebaseInstallationRequestResponseAuthToken
    fid: str
    name: str
    refreshToken: str


class RegisterInstallRequestBody(BaseModel):
    app_public_key: str
    app_package: str  # aka appGroup
    app_name: str
    app_cert: str
    user_agent: str
    json_body: RegisterInstallRequestBodyJsonBody


class RegisterGcmRequestBodyJsonBody(BaseModel):
    x_subtype: str = Field(serialization_alias="X-subtype")
    sender: str
    x_appid: str = Field(serialization_alias="X-appid")
    x_google_firebase_installations_auth: str = Field(serialization_alias="X-Goog-Firebase-Installations-Auth")
    app: str
    device: str

    @classmethod
    def from_models(
            cls,
            install_request_body: RegisterInstallRequestBody,
            install_request_response: FirebaseInstallationRequestResponse,
            check_in_request_response: CheckInResponseMessage
    ):
        sender: str = install_request_body.json_body.appId.split(":")[1]

        return cls(
            x_subtype=sender,
            sender=sender,
            x_appid=install_request_response.fid,
            x_google_firebase_installations_auth=install_request_response.authToken.token,
            app=install_request_body.app_package,
            device=str(check_in_request_response.android_id),
        )


class RegisterGcmRequestBody(BaseModel):
    json_body: RegisterGcmRequestBodyJsonBody
    user_agent: str

    # Via Check-in
    android_id: str
    security_token: str

    @classmethod
    def from_models(
            cls,
            install_request_body: RegisterInstallRequestBody,
            install_request_response: FirebaseInstallationRequestResponse,
            check_in_request_response: CheckInResponseMessage
    ):
        return cls(
            json_body=RegisterGcmRequestBodyJsonBody.from_models(
                install_request_body=install_request_body,
                install_request_response=install_request_response,
                check_in_request_response=check_in_request_response
            ),
            android_id=str(check_in_request_response.android_id),
            security_token=str(check_in_request_response.security_token),
            user_agent=install_request_body.user_agent
        )


class RegisterGcmRequestResponse(BaseModel):
    # Either error is token is populated
    token: str | None = None
    error: str | None = None
