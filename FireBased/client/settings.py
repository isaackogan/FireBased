from dataclasses import dataclass, field

# Headers to send the Google overlords
CHECK_IN_HEADERS: dict[str, str] = {
    "Content-type": "application/x-protobuffer",
    "Accept-Encoding": "gzip",
    "User-Agent": "Android-Checkin/2.0 (vbox86p JLS36G); gzip"
}

REGISTER_INSTALL_HEADERS: dict[str, str] = {
    "Content-Type": "application/json",
}


@dataclass()
class _FireBasedSettings:
    check_in_url: str = "https://android.clients.google.com/checkin"
    check_in_headers: dict[str, str] = field(default_factory=lambda: CHECK_IN_HEADERS)
    register_install_url: str = "https://firebaseinstallations.googleapis.com/v1/projects/{appName}/installations"
    register_install_headers: dict[str, str] = field(default_factory=lambda: REGISTER_INSTALL_HEADERS)
    register_gcm_url: str = "https://android.apis.google.com/c2dm/register3"
    http_client_ja3: str = "771,4865-4866-4867-49195-49196-52393-49199-49200-52392-49171-49172-156-157-47-53,0-23-65281-10-11-35-16-5-13-51-45-43,29-23-24,0"


FireBasedSettings = _FireBasedSettings()

__all__ = [
    "CHECK_IN_HEADERS",
    "FireBasedSettings"
]
