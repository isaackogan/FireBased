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
    register_gcm_url = "https://android.apis.google.com/c2dm/register3"


FireBasedSettings = _FireBasedSettings()

__all__ = [
    "CHECK_IN_HEADERS",
    "FireBasedSettings"
]


