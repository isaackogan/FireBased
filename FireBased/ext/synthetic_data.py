import random
from string import hexdigits
from typing import TypedDict

from FireBased.client.proto import CheckInRequestMessageCheckInBuild, CheckInRequestMessageCheckIn, CheckInRequestMessage, CheckInRequestMessageDeviceConfig, CheckInRequestMessageDeviceConfigFeatureVersion
from FireBased.ext import synthetics


class BuildDetail(TypedDict):
    # $(BRAND)/$(PRODUCT)/$(DEVICE)/$(BOARD):$(VERSION.RELEASE)/$(ID)/$(VERSION.INCREMENTAL):$(TYPE)/$(TAGS)
    fingerprint: str
    hardware: str
    brand: str
    radio: str
    client_id: str


def luhn_checksum(number) -> int:
    """Calculate the Luhn checksum digit for a number."""

    def digits_of(n):
        return [int(d) for d in str(n)]

    digits = digits_of(number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d * 2))
    return checksum % 10


def generate_imei() -> str:
    """Generate a valid IMEI number."""
    # Base IMEI (14 digits)
    imei_base = [random.randint(0, 9) for _ in range(14)]
    imei_str = ''.join(map(str, imei_base))

    # Calculate the check digit
    check_digit = (10 - luhn_checksum(int(imei_str))) % 10
    imei_base.append(check_digit)

    return ''.join(map(str, imei_base))


def create_synthetic_check_in(
        build_override: CheckInRequestMessageCheckInBuild | None = None,
) -> CheckInRequestMessage:
    # Create build
    random_build: BuildDetail = random.choice(list(synthetics.DEVICE_BUILDS.values()))
    random_build |= {"sdk_version": 33, "package_version_code": 245034032}
    check_in_build = build_override or CheckInRequestMessageCheckInBuild().from_pydict(random_build)

    # Borrowed from https://github.com/mxrch/ghunt-v3 with thanks <3
    return CheckInRequestMessage(
        imei=generate_imei(),
        android_id=0,
        digest="1",  # It makes the server dropping a list of interesting settings values 🥰
        locale="en",
        logging_id=random.getrandbits(63),
        mac_address=["".join(random.choices("0123456789abcdef", k=12))],
        meid="".join(random.choices("0123456789", k=14)),
        account_cookie=[""],
        time_zone="GMT",
        version=3,
        ota_cert=["--no-output--"],
        esn="".join(random.choice(hexdigits) for _ in range(8)),
        mac_address_type=["wifi"],
        device_configuration=CheckInRequestMessageDeviceConfig(
            touch_screen=3,
            keyboard_type=1,
            navigation=1,
            screen_layout=2,
            has_hard_keyboard=True,
            has_five_way_navigation=True,
            density_dpi=320,
            gl_es_version=131072,
            gl_extension=synthetics.GL_EXTENSIONS,
            shared_library=synthetics.SHARED_LIBRARIES,
            available_feature=synthetics.FEATURES,
            native_platform=synthetics.NATIVE_PLATFORMS,
            locale=synthetics.LOCALES,
            width_pixels=720,
            height_pixels=1280,
            feature_version=[
                CheckInRequestMessageDeviceConfigFeatureVersion(
                    name=k, version=v
                ) for k, v in synthetics.FEATURES_VERSIONS.items()
            ]
        ),
        fragment=0,
        user_serial_number=0,
        checkin=CheckInRequestMessageCheckIn(
            build=check_in_build,
            last_checkin_ms=0
        )
    )


def create_mobile_user_agent() -> str:
    """
    User agent in format
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Build/TQ3A.230901.001)",

    """

    device, _ = random.choice(list(synthetics.DEVICE_BUILDS.items()))
    return f"Dalvik/2.1.0 (Linux; U; Android 13; {device} Build/TQ3A.230901.001)"
