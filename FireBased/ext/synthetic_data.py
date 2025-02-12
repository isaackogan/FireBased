import random
from string import hexdigits
from typing import TypedDict

from FireBased.client.proto import CheckInRequestMessageCheckInBuild, CheckInRequestMessageCheckIn, CheckInRequestMessage


class BuildDetail(TypedDict):
    fingerprint: str
    hardware: str
    brand: str
    radio: str
    client_id: str


DEVICE_BUILD_DETAILS: dict[str, BuildDetail] = {
    "Galaxy S21": {
        "fingerprint": "samsung/o1sxxx/o1s:12/SP1A.210812.016/123456:user/release-keys",
        "hardware": "exynos2100",
        "brand": "Samsung",
        "radio": "G991BXXU3AUE1",
        "client_id": "android-samsung"
    },
    "Xperia 1 III": {
        "fingerprint": "sony/pdx215/pdx215:12/SP1A.210812.016/123456:user/release-keys",
        "hardware": "snapdragon888",
        "brand": "Sony",
        "radio": "58.1.A.5.159",
        "client_id": "android-sony"
    },
    "Mi 11": {
        "fingerprint": "xiaomi/venus/venus:12/SP1A.210812.016/123456:user/release-keys",
        "hardware": "venus",
        "brand": "Xiaomi",
        "radio": "MIXM",
        "client_id": "android-xiaomi"
    },
    "OnePlus 9": {
        "fingerprint": "oneplus/lemonade/lemonade:12/SP1A.210812.016/123456:user/release-keys",
        "hardware": "lemonade",
        "brand": "OnePlus",
        "radio": "11.2.5.5.LE15AA",
        "client_id": "android-oneplus"
    },
    "Nokia 8.3": {
        "fingerprint": "nokia/nbg/nokia8.3:12/SP1A.210812.016/123456:user/release-keys",
        "hardware": "nbg",
        "brand": "Nokia",
        "radio": "V2.390",
        "client_id": "android-nokia"
    },
    "Moto G Power": {
        "fingerprint": "motorola/rayford/rayford:12/SP1A.210812.016/123456:user/release-keys",
        "hardware": "rayford",
        "brand": "Motorola",
        "radio": "GPP5",
        "client_id": "android-motorola"
    },
    "P40 Pro": {
        "fingerprint": "huawei/els-nx9/els:12/SP1A.210812.016/123456:user/release-keys",
        "hardware": "kirin990",
        "brand": "Huawei",
        "radio": "ELS-NX9",
        "client_id": "android-huawei"
    },
    "Find X3": {
        "fingerprint": "oppo/PEEM00/PEEM00:12/SP1A.210812.016/123456:user/release-keys",
        "hardware": "snapdragon888",
        "brand": "Oppo",
        "radio": "PEEM00",
        "client_id": "android-oppo"
    },
    "V60 ThinQ": {
        "fingerprint": "lge/lmv600lm/lmv600lm:12/SP1A.210812.016/123456:user/release-keys",
        "hardware": "lmv600",
        "brand": "LG",
        "radio": "V600TM20a",
        "client_id": "android-lg"
    },
    "Redmi Note 10": {
        "fingerprint": "xiaomi/mojito/mojito:12/SP1A.210812.016/123456:user/release-keys",
        "hardware": "mojito",
        "brand": "Xiaomi",
        "radio": "QJUMIXM",
        "client_id": "android-xiaomi"
    },
    "Reno 6": {
        "fingerprint": "oppo/CPH2251/CPH2251:12/SP1A.210812.016/123456:user/release-keys",
        "hardware": "CPH2251",
        "brand": "Oppo",
        "radio": "CPH2251",
        "client_id": "android-oppo"
    },
    "Pixel 5": {
        "fingerprint": "google/redfin/redfin:12/SP1A.210812.016/123456:user/release-keys",
        "hardware": "redfin",
        "brand": "Google",
        "radio": "G77x",
        "client_id": "android-google"
    },
    "Galaxy Note 20": {
        "fingerprint": "samsung/c1xxx/c1:12/SP1A.210812.016/123456:user/release-keys",
        "hardware": "exynos990",
        "brand": "Samsung",
        "radio": "N986BXXS2AUE2",
        "client_id": "android-samsung"
    },
    "ROG Phone 5": {
        "fingerprint": "asus/ZS673KS/ZS673KS:12/SP1A.210812.016/123456:user/release-keys",
        "hardware": "ZS673KS",
        "brand": "Asus",
        "radio": "18.0840.2106.87",
        "client_id": "android-asus"
    },
    "Magic 3": {
        "fingerprint": "honor/ELZ-AN00/ELZ-AN00:12/SP1A.210812.016/123456:user/release-keys",
        "hardware": "snapdragon888",
        "brand": "Honor",
        "radio": "ELZ-AN00",
        "client_id": "android-honor"
    },
    "sdk_gphone64_arm64": {
        "fingerprint": "google/sdk_gphone64_arm64/emulator64_arm64:13/TP1A.220624.014/1234567:user/release-keys",
        "hardware": "emulator64_arm64",
        "brand": "Google",
        "radio": "",
        "client_id": "android-google"
    }
}


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
    random_build: BuildDetail = random.choice(list(DEVICE_BUILD_DETAILS.values()))
    check_in_build = build_override or CheckInRequestMessageCheckInBuild().from_pydict(random_build)

    # Build container
    check_in_build_container: CheckInRequestMessageCheckIn = CheckInRequestMessageCheckIn()
    check_in_build_container.build = check_in_build
    check_in_build_container.last_check_in_ms = 0

    # Main object, randomly generate items
    message_data = {
        "imei": str(generate_imei()),
        "android_id": 0,
        "locale": "en",
        "logging_id": random.getrandbits(63),
        "mac_address": ["".join(random.choices("0123456789abcdef", k=12))],
        "meid": "".join(random.choices("0123456789", k=14)),
        "account_cookie": [""],
        "time_zone": "GMT",
        "version": 3,
        "ota_cert": ["--no-output--"],
        "esn": "".join(random.choice(hexdigits) for _ in range(8)),
        "mac_address_type": ["wifi"],
        "fragment": 0,
        "user_serial_number": 0
    }

    message_data = {'imei': '253125236601099', 'android_id': 0, 'locale': 'en', 'logging_id': 2805036932279879224, 'mac_address': ['46463669c9ba'], 'meid': '49805837553036', 'account_cookie': [''], 'time_zone': 'GMT', 'version': 3,
                    'ota_cert': ['--no-output--'], 'esn': 'Ea870AE2', 'mac_address_type': ['wifi'], 'fragment': 0, 'user_serial_number': 0}

    base_message: CheckInRequestMessage = CheckInRequestMessage().from_pydict(message_data)

    base_message.check_in = check_in_build_container
    return base_message


# $(BRAND)/$(PRODUCT)/$(DEVICE)/$(BOARD):$(VERSION.RELEASE)/$(ID)/$(VERSION.INCREMENTAL):$(TYPE)/$(TAGS)

DEVICE_MANUFACTURER_LIST: list[tuple[str, str]] = [
    ("Galaxy S21", "Samsung"),
    ("Xperia 1 III", "Sony"),
    ("Mi 11", "Xiaomi"),
    ("OnePlus 9", "OnePlus"),
    ("Nokia 8.3", "Nokia"),
    ("Moto G Power", "Motorola"),
    ("P40 Pro", "Huawei"),
    ("Find X3", "Oppo"),
    ("V60 ThinQ", "LG"),
    ("Redmi Note 10", "Xiaomi"),
    ("Reno 6", "Oppo"),
    ("Pixel 5", "Google"),
    ("Galaxy Note 20", "Samsung"),
    ("ROG Phone 5", "Asus"),
    ("Magic 3", "Honor"),
]


def create_mobile_user_agent() -> str:
    """
    User agent in format
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 13; Pixel 6 Build/TQ3A.230901.001)",

    """

    device, manufacturer = random.choice(DEVICE_MANUFACTURER_LIST)
    return f"Dalvik/2.1.0 (Linux; U; Android 13; {device} Build/TQ3A.230901.001)"
