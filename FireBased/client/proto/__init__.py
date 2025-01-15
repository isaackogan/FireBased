# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: firebase.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass
from typing import List

import betterproto


@dataclass(eq=False, repr=False)
class CheckInRequestMessage(betterproto.Message):
    imei: str = betterproto.string_field(1)
    android_id: int = betterproto.int64_field(2)
    digest: str = betterproto.string_field(3)
    check_in: "CheckInRequestMessageCheckIn" = betterproto.message_field(4)
    desired_build: str = betterproto.string_field(5)
    locale: str = betterproto.string_field(6)
    logging_id: int = betterproto.int64_field(7)
    market_checkin: str = betterproto.string_field(8)
    mac_address: List[str] = betterproto.string_field(9)
    meid: str = betterproto.string_field(10)
    account_cookie: List[str] = betterproto.string_field(11)
    time_zone: str = betterproto.string_field(12)
    security_token: int = betterproto.fixed64_field(13)
    version: int = betterproto.int32_field(14)
    ota_cert: List[str] = betterproto.string_field(15)
    serial: str = betterproto.string_field(16)
    esn: str = betterproto.string_field(17)
    device_configuration: "CheckInRequestMessageDeviceConfig" = (
        betterproto.message_field(18)
    )
    mac_address_type: List[str] = betterproto.string_field(19)
    fragment: int = betterproto.int32_field(20)
    user_name: str = betterproto.string_field(21)
    user_serial_number: int = betterproto.int32_field(22)


@dataclass(eq=False, repr=False)
class CheckInRequestMessageCheckIn(betterproto.Message):
    build: "CheckInRequestMessageCheckInBuild" = betterproto.message_field(1)
    last_checkin_ms: int = betterproto.int64_field(2)
    stat: List["CheckInRequestMessageCheckInStatistic"] = betterproto.message_field(4)
    requested_group: List[str] = betterproto.string_field(5)
    cell_operator: str = betterproto.string_field(6)
    sim_operator: str = betterproto.string_field(7)
    roaming: str = betterproto.string_field(8)
    user_number: int = betterproto.int32_field(9)


@dataclass(eq=False, repr=False)
class CheckInRequestMessageCheckInBuild(betterproto.Message):
    fingerprint: str = betterproto.string_field(1)
    hardware: str = betterproto.string_field(2)
    brand: str = betterproto.string_field(3)
    radio: str = betterproto.string_field(4)
    bootloader: str = betterproto.string_field(5)
    client_id: str = betterproto.string_field(6)
    time: int = betterproto.int64_field(7)
    package_version_code: int = betterproto.int32_field(8)
    device: str = betterproto.string_field(9)
    sdk_version: int = betterproto.int32_field(10)
    model: str = betterproto.string_field(11)
    manufacturer: str = betterproto.string_field(12)
    product: str = betterproto.string_field(13)
    ota_installed: bool = betterproto.bool_field(14)


@dataclass(eq=False, repr=False)
class CheckInRequestMessageCheckInEvent(betterproto.Message):
    tag: str = betterproto.string_field(1)
    value: str = betterproto.string_field(2)
    time_ms: int = betterproto.int64_field(3)


@dataclass(eq=False, repr=False)
class CheckInRequestMessageCheckInStatistic(betterproto.Message):
    tag: str = betterproto.string_field(1)
    count: int = betterproto.int32_field(2)
    sum: float = betterproto.float_field(3)


@dataclass(eq=False, repr=False)
class CheckInRequestMessageDeviceConfig(betterproto.Message):
    touch_screen: int = betterproto.int32_field(1)
    keyboard_type: int = betterproto.int32_field(2)
    navigation: int = betterproto.int32_field(3)
    screen_layout: int = betterproto.int32_field(4)
    has_hard_keyboard: bool = betterproto.bool_field(5)
    has_five_way_navigation: bool = betterproto.bool_field(6)
    density_dpi: int = betterproto.int32_field(7)
    gl_es_version: int = betterproto.int32_field(8)
    shared_library: List[str] = betterproto.string_field(9)
    available_feature: List[str] = betterproto.string_field(10)
    native_platform: List[str] = betterproto.string_field(11)
    width_pixels: int = betterproto.int32_field(12)
    height_pixels: int = betterproto.int32_field(13)
    locale: List[str] = betterproto.string_field(14)
    gl_extension: List[str] = betterproto.string_field(15)
    device_class: int = betterproto.int32_field(16)
    max_apk_download_size_mb: int = betterproto.int32_field(17)


@dataclass(eq=False, repr=False)
class CheckInResponseMessage(betterproto.Message):
    stats_ok: bool = betterproto.bool_field(1)
    intent: List["CheckInResponseMessageIntent"] = betterproto.message_field(2)
    time_ms: int = betterproto.int64_field(3)
    digest: str = betterproto.string_field(4)
    setting: List["CheckInResponseMessageGServicesSetting"] = betterproto.message_field(
        5
    )
    market_ok: bool = betterproto.bool_field(6)
    android_id: int = betterproto.fixed64_field(7)
    security_token: int = betterproto.fixed64_field(8)
    settings_diff: bool = betterproto.bool_field(9)
    delete_setting: List[str] = betterproto.string_field(10)
    version_info: str = betterproto.string_field(11)
    device_data_version_info: str = betterproto.string_field(12)


@dataclass(eq=False, repr=False)
class CheckInResponseMessageIntent(betterproto.Message):
    action: str = betterproto.string_field(1)
    data_uri: str = betterproto.string_field(2)
    mime_type: str = betterproto.string_field(3)
    java_class: str = betterproto.string_field(4)
    extra: List["CheckInResponseMessageIntentExtra"] = betterproto.message_field(5)


@dataclass(eq=False, repr=False)
class CheckInResponseMessageIntentExtra(betterproto.Message):
    name: str = betterproto.string_field(6)
    value: str = betterproto.string_field(7)


@dataclass(eq=False, repr=False)
class CheckInResponseMessageGServicesSetting(betterproto.Message):
    name: bytes = betterproto.bytes_field(1)
    value: bytes = betterproto.bytes_field(2)