# For the Android checkin


DEVICE_BUILDS: dict[str, dict[str, str]] = {
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
    "sdk_gphone64_arm64 ": {
        "fingerprint": "google/sdk_gphone64_arm64/emulator64_arm64:13/TP1A.220624.014/1234567:user/release-keys",
        "hardware": "emulator64_arm64",
        "brand": "Google",
        "radio": "",
        "client_id": "android-google"
    }
}

FEATURES = [
    'android.hardware.bluetooth',
    'android.hardware.camera',
    'android.hardware.camera.autofocus',
    'android.hardware.camera.flash',
    'android.hardware.camera.front',
    'android.hardware.faketouch',
    'android.hardware.location',
    'android.hardware.location.gps',
    'android.hardware.location.network',
    'android.hardware.microphone',
    'android.hardware.nfc',
    'android.hardware.screen.landscape',
    'android.hardware.screen.portrait',
    'android.hardware.sensor.accelerometer',
    'android.hardware.sensor.barometer',
    'android.hardware.sensor.compass',
    'android.hardware.sensor.gyroscope',
    'android.hardware.sensor.light',
    'android.hardware.sensor.proximity',
    'android.hardware.telephony',
    'android.hardware.telephony.gsm',
    'android.hardware.touchscreen',
    'android.hardware.touchscreen.multitouch',
    'android.hardware.touchscreen.multitouch.distinct',
    'android.hardware.touchscreen.multitouch.jazzhand',
    'android.hardware.usb.accessory',
    'android.hardware.usb.host',
    'android.hardware.wifi',
    'android.hardware.wifi.direct',
    'android.software.live_wallpaper',
    'android.software.sip',
    'android.software.sip.voip',
    'com.google.android.feature.GOOGLE_BUILD',
    'com.nxp.mifare',
    'android.software.midi',
    'android.software.device_admin',
    'android.hardware.opengles.aep',
    'android.hardware.bluetooth_le'
]

FEATURES_VERSIONS = {
    'android.hardware.audio.output': 0,
    'android.hardware.bluetooth': 0,
    'android.hardware.bluetooth_le': 0,
    'android.hardware.camera': 0,
    'android.hardware.camera.any': 0,
    'android.hardware.camera.front': 0,
    'android.hardware.ethernet': 0,
    'android.hardware.faketouch': 0,
    'android.hardware.faketouch.multitouch.distinct': 0,
    'android.hardware.faketouch.multitouch.jazzhand': 0,
    'android.hardware.gamepad': 0,
    'android.hardware.hardware_keystore': 41,
    'android.hardware.location': 0,
    'android.hardware.location.gps': 0,
    'android.hardware.location.network': 0,
    'android.hardware.microphone': 0,
    'android.hardware.ram.normal': 0,
    'android.hardware.screen.landscape': 0,
    'android.hardware.screen.portrait': 0,
    'android.hardware.touchscreen': 0,
    'android.hardware.touchscreen.multitouch': 0,
    'android.hardware.touchscreen.multitouch.distinct': 0,
    'android.hardware.type.pc': 0,
    'android.hardware.usb.accessory': 0,
    'android.hardware.usb.host': 0,
    'android.hardware.vulkan.level': 0,
    'android.hardware.vulkan.version': 4198400,
    'android.hardware.wifi': 0,
    'android.software.activities_on_secondary_displays': 0,
    'android.software.app_enumeration': 0,
    'android.software.app_widgets': 0,
    'android.software.autofill': 0,
    'android.software.cts': 0,
    'android.software.device_admin': 0,
    'android.software.erofs': 0,
    'android.software.freeform_window_management': 0,
    'android.software.incremental_delivery': 2,
    'android.software.ipsec_tunnels': 0,
    'android.software.managed_users': 0,
    'android.software.opengles.deqp.level': 132449025,
    'android.software.picture_in_picture': 0,
    'android.software.print': 0,
    'android.software.verified_boot': 0,
    'android.software.vulkan.deqp.level': 132514561,
    'android.software.webview': 0,
    'com.google.android.apps.dialer.SUPPORTED': 0,
    'com.google.android.feature.D2D_CABLE_MIGRATION_FEATURE': 0,
    'com.google.android.feature.EXCHANGE_6_2': 0,
    'com.google.android.feature.GOOGLE_BUILD': 0,
    'com.google.android.feature.GOOGLE_EXPERIENCE': 0,
}

GL_EXTENSIONS = [
    "GL_OES_compressed_ETC1_RGB8_texture",
    "GL_KHR_texture_compression_astc_ldr"
]

SHARED_LIBRARIES = [
    'android.test.runner',
    'com.android.future.usb.accessory',
    'com.android.location.provider',
    'com.android.nfc_extras',
    'com.google.android.maps',
    'com.google.android.media.effects',
    'com.google.widevine.software.drm',
    'javax.obex',
    'org.apache.http.legacy',
    'android.test.runner',
    'global-miui11-empty.jar'
]

NATIVE_PLATFORMS = [
    "armeabi-v7a",
    "armeabi",
    "arm64-v8a",
    "x86"
]

LOCALES = [
    "af",
    "af-ZA",
    "am",
    "am-ET",
    "ar",
    "ar-EG",
    "ar-XB",
    "as",
    "az",
    "az-AZ",
    "be",
    "bg",
    "bg-BG",
    "bn",
    "bs",
    "bs-BA",
    "ca",
    "ca-ES",
    "cs",
    "cs-CZ",
    "da",
    "da-DK",
    "de",
    "de-DE",
    "el",
    "el-GR",
    "en",
    "en-AU",
    "en-CA",
    "en-GB",
    "en-IN",
    "en-US",
    "en-XA",
    "es",
    "es-ES",
    "es-US",
    "et",
    "et-EE",
    "eu",
    "eu-ES",
    "fa",
    "fa-IR",
    "fi",
    "fi-FI",
    "fil",
    "fil-PH",
    "fr",
    "fr-CA",
    "fr-FR",
    "gl",
    "gl-ES",
    "gu",
    "hi",
    "hi-IN",
    "hr",
    "hr-HR",
    "hu",
    "hu-HU",
    "hy",
    "in",
    "in-ID",
    "is",
    "is-IS",
    "it",
    "it-IT",
    "iw",
    "iw-IL",
    "ja",
    "ja-JP",
    "ka",
    "ka-GE",
    "kk",
    "kk-KZ",
    "km",
    "kn",
    "ko",
    "ko-KR",
    "ky",
    "lo",
    "lt",
    "lt-LT",
    "lv",
    "lv-LV",
    "mk",
    "ml",
    "mn",
    "mr",
    "ms",
    "ms-MY",
    "my",
    "nb",
    "nb-NO",
    "ne",
    "nl",
    "nl-NL",
    "or",
    "pa",
    "pl",
    "pl-PL",
    "pt",
    "pt-BR",
    "pt-PT",
    "ro",
    "ro-RO",
    "ru",
    "ru-RU",
    "si",
    "sk",
    "sk-SK",
    "sl",
    "sl-SI",
    "sq",
    "sq-AL",
    "sr",
    "sr-Latn",
    "sr-RS",
    "sv",
    "sv-SE",
    "sw",
    "sw-TZ",
    "ta",
    "te",
    "th",
    "th-TH",
    "tr",
    "tr-TR",
    "uk",
    "uk-UA",
    "ur",
    "uz",
    "vi",
    "vi-VN",
    "zh-CN",
    "zh-HK",
    "zh-TW",
    "zu",
    "zu-ZA"
]

DEVICES = [
    {
        "android_version": 15,
        "device_name": "Pixel 9 Pro XL",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250205.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 9 Pro XL Build/AP4A.250205.002)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 9 Pro Fold",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250205.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 9 Pro Fold Build/AP4A.250205.002)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 9 Pro",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250205.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 9 Pro Build/AP4A.250205.002)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 9",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250205.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 9 Build/AP4A.250205.002)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 8a",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250205.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 8a Build/AP4A.250205.002)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 8 Pro",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250205.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 8 Pro Build/AP4A.250205.002)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 8",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250205.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 8 Build/AP4A.250205.002)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 7a",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250205.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 7a Build/AP4A.250205.002)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 7 Pro",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250205.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 7 Pro Build/AP4A.250205.002)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 7",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250205.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 7 Build/AP4A.250205.002)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 6 Pro",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250205.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 6 Pro Build/AP4A.250205.002)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 6a",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250205.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 6a Build/AP4A.250205.002)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 6",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250205.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 6 Build/AP4A.250205.002)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel Fold",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250205.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel Fold Build/AP4A.250205.002)"
    },
    {
        "android_version": 14,
        "device_name": "Pixel 5a (5G)",
        "device_manufacturer": "Google",
        "device_software_build": "AP2A.240805.005",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Pixel 5a (5G) Build/AP2A.240805.005)"
    },
    {
        "android_version": 14,
        "device_name": "Pixel 9 Pro XL",
        "device_manufacturer": "Google",
        "device_software_build": "AD1A.240905.004",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Pixel 9 Pro XL Build/AD1A.240905.004)"
    },
    {
        "android_version": 14,
        "device_name": "Pixel 9 Pro Fold",
        "device_manufacturer": "Google",
        "device_software_build": "AD1A.240905.004",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Pixel 9 Pro Fold Build/AD1A.240905.004)"
    },
    {
        "android_version": 14,
        "device_name": "Pixel 9 Pro",
        "device_manufacturer": "Google",
        "device_software_build": "AD1A.240905.004",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Pixel 9 Pro Build/AD1A.240905.004)"
    },
    {
        "android_version": 14,
        "device_name": "Pixel 9",
        "device_manufacturer": "Google",
        "device_software_build": "AD1A.240905.004",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Pixel 9 Build/AD1A.240905.004)"
    },
    {
        "android_version": 14,
        "device_name": "Pixel 9 Pro",
        "device_manufacturer": "Google",
        "device_software_build": "AD1A.240905.004",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Pixel 9 Pro Build/AD1A.240905.004)"
    },
    {
        "android_version": 14,
        "device_name": "Pixel 9 Pro Fold",
        "device_manufacturer": "Google",
        "device_software_build": "AD1A.240905.004",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Pixel 9 Pro Fold Build/AD1A.240905.004)"
    },
    {
        "android_version": 14,
        "device_name": "Pixel 9 Pro XL",
        "device_manufacturer": "Google",
        "device_software_build": "AD1A.240905.004",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Pixel 9 Pro XL Build/AD1A.240905.004)"
    },
    {
        "android_version": 14,
        "device_name": "Pixel 6",
        "device_manufacturer": "Google",
        "device_software_build": "AP2A.240905.003.F1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Pixel 6 Build/AP2A.240905.003.F1)"
    },
    {
        "android_version": 14,
        "device_name": "Pixel 6a",
        "device_manufacturer": "Google",
        "device_software_build": "AP2A.240905.003.F1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Pixel 6a Build/AP2A.240905.003.F1)"
    },
    {
        "android_version": 14,
        "device_name": "Pixel 6 Pro",
        "device_manufacturer": "Google",
        "device_software_build": "AP2A.240905.003.F1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Pixel 6 Pro Build/AP2A.240905.003.F1)"
    },
    {
        "android_version": 14,
        "device_name": "Pixel 8a",
        "device_manufacturer": "Google",
        "device_software_build": "AP2A.240905.003.E1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Pixel 8a Build/AP2A.240905.003.E1)"
    },
    {
        "android_version": 14,
        "device_name": "Pixel 8",
        "device_manufacturer": "Google",
        "device_software_build": "AP2A.240905.003.D1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Pixel 8 Build/AP2A.240905.003.D1)"
    },
    {
        "android_version": 14,
        "device_name": "Pixel 8 Pro",
        "device_manufacturer": "Google",
        "device_software_build": "AP2A.240905.003.D1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Pixel 8 Pro Build/AP2A.240905.003.D1)"
    },
    {
        "android_version": 14,
        "device_name": "Pixel 7",
        "device_manufacturer": "Google",
        "device_software_build": "AP2A.240905.003",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Pixel 7 Build/AP2A.240905.003)"
    },
    {
        "android_version": 14,
        "device_name": "Pixel 7a",
        "device_manufacturer": "Google",
        "device_software_build": "AP2A.240905.003",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Pixel 7a Build/AP2A.240905.003)"
    },
    {
        "android_version": 14,
        "device_name": "Pixel 7 Pro",
        "device_manufacturer": "Google",
        "device_software_build": "AP2A.240905.003",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Pixel 7 Pro Build/AP2A.240905.003)"
    },
    {
        "android_version": 14,
        "device_name": "Pixel Fold",
        "device_manufacturer": "Google",
        "device_software_build": "AP2A.240905.003",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Pixel Fold Build/AP2A.240905.003)"
    },
    {
        "android_version": 14,
        "device_name": "SM-A166W",
        "device_manufacturer": "Samsung",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SM-A166W Build/UP1A.231005.007)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 6a",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250205.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 6a Build/AP4A.250205.002)"
    },
    {
        "android_version": 15,
        "device_name": "motorola razr plus 2023",
        "device_manufacturer": "Motorola",
        "device_software_build": "V1TZ35H.41-21-3",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; motorola razr plus 2023 Build/V1TZ35H.41-21-3)"
    },
    {
        "android_version": 15,
        "device_name": "2304FPN6DG",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AQ3A.240912.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 2304FPN6DG Build/AQ3A.240912.001)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 8",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250205.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 8 Build/AP4A.250205.002)"
    },
    {
        "android_version": 14,
        "device_name": "XQ-CC72",
        "device_manufacturer": "Sony",
        "device_software_build": "65.2.A.2.224",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; XQ-CC72 Build/65.2.A.2.224)"
    },
    {
        "android_version": 15,
        "device_name": "M2012K11AG",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AP4A.250105.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; M2012K11AG Build/AP4A.250105.002)"
    },
    {
        "android_version": 15,
        "device_name": "motorola razr 40 ultra",
        "device_manufacturer": "Motorola",
        "device_software_build": "V1TZS35H.41-21-3-2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; motorola razr 40 ultra Build/V1TZS35H.41-21-3-2)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 6",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250205.002.A1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 6 Build/AP4A.250205.002.A1)"
    },
    {
        "android_version": 15,
        "device_name": "SM-S938N",
        "device_manufacturer": "Samsung",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; SM-S938N Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 14,
        "device_name": "moto g(7)",
        "device_manufacturer": "Motorola",
        "device_software_build": "AP2A.240905.003",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g(7) Build/AP2A.240905.003)"
    },
    {
        "android_version": 15,
        "device_name": "2405CRPFDG",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AQ3A.240912.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 2405CRPFDG Build/AQ3A.240912.001)"
    },
    {
        "android_version": 14,
        "device_name": "moto g stylus 5G - 2024",
        "device_manufacturer": "Motorola",
        "device_software_build": "U2UBS34.44-86-5",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g stylus 5G - 2024 Build/U2UBS34.44-86-5)"
    },
    {
        "android_version": 15,
        "device_name": "XQ-DC72",
        "device_manufacturer": "Sony",
        "device_software_build": "68.2.A.2.38A",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; XQ-DC72 Build/68.2.A.2.38A)"
    },
    {
        "android_version": 15,
        "device_name": "SM-S926U1",
        "device_manufacturer": "Samsung",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; SM-S926U1 Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 14,
        "device_name": "SHG12",
        "device_manufacturer": "Sharp",
        "device_software_build": "SC121",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SHG12 Build/SC121)"
    },
    {
        "android_version": 15,
        "device_name": "SM-S931W",
        "device_manufacturer": "Samsung",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; SM-S931W Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 14,
        "device_name": "moto g 5G plus",
        "device_manufacturer": "Motorola",
        "device_software_build": "AP2A.240905.003",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g 5G plus Build/AP2A.240905.003)"
    },
    {
        "android_version": 14,
        "device_name": "SO-52E",
        "device_manufacturer": "Sony",
        "device_software_build": "70.0.B.3.184",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SO-52E Build/70.0.B.3.184)"
    },
    {
        "android_version": 14,
        "device_name": "BV8200",
        "device_manufacturer": "Blackview",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; BV8200 Build/UP1A.231005.007)"
    },
    {
        "android_version": 15,
        "device_name": "2107113SG",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AP4A.250105.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 2107113SG Build/AP4A.250105.002)"
    },
    {
        "android_version": 15,
        "device_name": "CPH2447",
        "device_manufacturer": "Oppo",
        "device_software_build": "TP1A.220905.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; CPH2447 Build/TP1A.220905.001)"
    },
    {
        "android_version": 15,
        "device_name": "SM-S938W",
        "device_manufacturer": "Samsung",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; SM-S938W Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 14,
        "device_name": "moto g54 5G",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TDS34.94-12-7-9",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g54 5G Build/U1TDS34.94-12-7-9)"
    },
    {
        "android_version": 14,
        "device_name": "motorola razr plus 2023",
        "device_manufacturer": "Motorola",
        "device_software_build": "U3TZS34.2-75-1-8",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; motorola razr plus 2023 Build/U3TZS34.2-75-1-8)"
    },
    {
        "android_version": 14,
        "device_name": "motorola razr plus 2024",
        "device_manufacturer": "Motorola",
        "device_software_build": "U3UXS34.56-124-1-1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; motorola razr plus 2024 Build/U3UXS34.56-124-1-1)"
    },
    {
        "android_version": 14,
        "device_name": "moto g 5G - 2023",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TPNS34.26-78-3-13",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g 5G - 2023 Build/U1TPNS34.26-78-3-13)"
    },
    {
        "android_version": 14,
        "device_name": "moto g64 5G",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TDS34.100-46-7-3",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g64 5G Build/U1TDS34.100-46-7-3)"
    },
    {
        "android_version": 14,
        "device_name": "moto g stylus 5G - 2023",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TGNS34.42-86-3-10",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g stylus 5G - 2023 Build/U1TGNS34.42-86-3-10)"
    },
    {
        "android_version": 15,
        "device_name": "XQ-DC54",
        "device_manufacturer": "Sony",
        "device_software_build": "68.2.A.2.38A",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; XQ-DC54 Build/68.2.A.2.38A)"
    },
    {
        "android_version": 14,
        "device_name": "SM-S166V",
        "device_manufacturer": "Samsung",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SM-S166V Build/UP1A.231005.007)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 8 Pro",
        "device_manufacturer": "Google",
        "device_software_build": "BP11.241121.013",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 8 Pro Build/BP11.241121.013)"
    },
    {
        "android_version": 14,
        "device_name": "moto g55 5G",
        "device_manufacturer": "Motorola",
        "device_software_build": "U3UTS34.44-73-4-2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g55 5G Build/U3UTS34.44-73-4-2)"
    },
    {
        "android_version": 14,
        "device_name": "NX724J",
        "device_manufacturer": "Nubia",
        "device_software_build": "UKQ1.230917.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; NX724J Build/UKQ1.230917.001)"
    },
    {
        "android_version": 15,
        "device_name": "23116PN5BC",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AQ3A.240627.003",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 23116PN5BC Build/AQ3A.240627.003)"
    },
    {
        "android_version": 15,
        "device_name": "SM-S936B",
        "device_manufacturer": "Samsung",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; SM-S936B Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 15,
        "device_name": "V2359A",
        "device_manufacturer": "Vivo",
        "device_software_build": "AP3A.240905.015.A1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; V2359A Build/AP3A.240905.015.A1)"
    },
    {
        "android_version": 14,
        "device_name": "BV7300",
        "device_manufacturer": "Blackview",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; BV7300 Build/UP1A.231005.007)"
    },
    {
        "android_version": 14,
        "device_name": "moto g34 5G",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1UGS34.23-110-23-4",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g34 5G Build/U1UGS34.23-110-23-4)"
    },
    {
        "android_version": 14,
        "device_name": "moto g 5G - 2024",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1UFN34.41-98-10-5",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g 5G - 2024 Build/U1UFN34.41-98-10-5)"
    },
    {
        "android_version": 14,
        "device_name": "XQ-CQ54",
        "device_manufacturer": "Sony",
        "device_software_build": "64.2.A.2.235",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; XQ-CQ54 Build/64.2.A.2.235)"
    },
    {
        "android_version": 14,
        "device_name": "moto g stylus 5G - 2024",
        "device_manufacturer": "Motorola",
        "device_software_build": "U2UBS34.44-57-1-1-4",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g stylus 5G - 2024 Build/U2UBS34.44-57-1-1-4)"
    },
    {
        "android_version": 14,
        "device_name": "XQ-CT54",
        "device_manufacturer": "Sony",
        "device_software_build": "64.2.A.2.235",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; XQ-CT54 Build/64.2.A.2.235)"
    },
    {
        "android_version": 14,
        "device_name": "BV6200 Plus",
        "device_manufacturer": "Blackview",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; BV6200 Plus Build/UP1A.231005.007)"
    },
    {
        "android_version": 15,
        "device_name": "XQ-DE54",
        "device_manufacturer": "Sony",
        "device_software_build": "67.2.A.2.41",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; XQ-DE54 Build/67.2.A.2.41)"
    },
    {
        "android_version": 14,
        "device_name": "moto g 5G - 2023",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TPNS34.26-78-10-1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g 5G - 2023 Build/U1TPNS34.26-78-10-1)"
    },
    {
        "android_version": 14,
        "device_name": "Armor X31 Pro",
        "device_manufacturer": "Ulefone",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Armor X31 Pro Build/UP1A.231005.007)"
    },
    {
        "android_version": 14,
        "device_name": "motorola razr 2024",
        "device_manufacturer": "Motorola",
        "device_software_build": "U3UCS34.63-88-12-3",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; motorola razr 2024 Build/U3UCS34.63-88-12-3)"
    },
    {
        "android_version": 15,
        "device_name": "2310FPCA4I",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 2310FPCA4I Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 15,
        "device_name": "SM-S931B",
        "device_manufacturer": "Samsung",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; SM-S931B Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 14,
        "device_name": "Mi 9T",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AP2A.240905.003.F1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Mi 9T Build/AP2A.240905.003.F1)"
    },
    {
        "android_version": 14,
        "device_name": "TECNO AD9",
        "device_manufacturer": "Tecno",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; TECNO AD9 Build/UP1A.231005.007)"
    },
    {
        "android_version": 14,
        "device_name": "moto g stylus (2023)",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1THS34.65-74-1-7-3",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g stylus (2023) Build/U1THS34.65-74-1-7-3)"
    },
    {
        "android_version": 14,
        "device_name": "TECNO KL4h",
        "device_manufacturer": "Tecno",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; TECNO KL4h Build/UP1A.231005.007)"
    },
    {
        "android_version": 14,
        "device_name": "M2006J10C",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "UKQ1.231003.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; M2006J10C Build/UKQ1.231003.002)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 7 Pro",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250105.002.B1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 7 Pro Build/AP4A.250105.002.B1)"
    },
    {
        "android_version": 14,
        "device_name": "SM-L305U",
        "device_manufacturer": "Samsung",
        "device_software_build": "AW2E.240318.016",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SM-L305U Build/AW2E.240318.016)"
    },
    {
        "android_version": 14,
        "device_name": "moto g 5G - 2023",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TPNS34.26-48-6-3-4",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g 5G - 2023 Build/U1TPNS34.26-48-6-3-4)"
    },
    {
        "android_version": 14,
        "device_name": "moto g54 5G",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TDS34.94-12-9-10-2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g54 5G Build/U1TDS34.94-12-9-10-2)"
    },
    {
        "android_version": 14,
        "device_name": "moto g13",
        "device_manufacturer": "Motorola",
        "device_software_build": "UHAS34.29-9",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g13 Build/UHAS34.29-9)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 7",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250105.002.B1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 7 Build/AP4A.250105.002.B1)"
    },
    {
        "android_version": 14,
        "device_name": "RMX3940",
        "device_manufacturer": "Realme",
        "device_software_build": "UKQ1.231108.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; RMX3940 Build/UKQ1.231108.001)"
    },
    {
        "android_version": 15,
        "device_name": "23117RA68G",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 23117RA68G Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 14,
        "device_name": "SO-52D",
        "device_manufacturer": "Sony",
        "device_software_build": "68.1.B.2.290",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SO-52D Build/68.1.B.2.290)"
    },
    {
        "android_version": 14,
        "device_name": "moto g 5G - 2023",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TPNS34.26-48-2-11",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g 5G - 2023 Build/U1TPNS34.26-48-2-11)"
    },
    {
        "android_version": 14,
        "device_name": "SOG08",
        "device_manufacturer": "Sony",
        "device_software_build": "63.2.C.1.114",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SOG08 Build/63.2.C.1.114)"
    },
    {
        "android_version": 15,
        "device_name": "PTP-N49",
        "device_manufacturer": "Honor",
        "device_software_build": "HONORPTP-N49",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; PTP-N49 Build/HONORPTP-N49)"
    },
    {
        "android_version": 15,
        "device_name": "RMX3701",
        "device_manufacturer": "Realme",
        "device_software_build": "AP3A.240617.008",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; RMX3701 Build/AP3A.240617.008)"
    },
    {
        "android_version": 14,
        "device_name": "moto g53 5G",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TPS34.29-83-9-3",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g53 5G Build/U1TPS34.29-83-9-3)"
    },
    {
        "android_version": 14,
        "device_name": "XQ-ES72",
        "device_manufacturer": "Sony",
        "device_software_build": "70.0.A.3.169",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; XQ-ES72 Build/70.0.A.3.169)"
    },
    {
        "android_version": 15,
        "device_name": "2406ERN9CI",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AQ3A.240912.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 2406ERN9CI Build/AQ3A.240912.001)"
    },
    {
        "android_version": 14,
        "device_name": "SOG14",
        "device_manufacturer": "Sony",
        "device_software_build": "70.0.C.3.146",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SOG14 Build/70.0.C.3.146)"
    },
    {
        "android_version": 14,
        "device_name": "SH-52E",
        "device_manufacturer": "Sharp",
        "device_software_build": "SB271",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SH-52E Build/SB271)"
    },
    {
        "android_version": 15,
        "device_name": "SM-G970F",
        "device_manufacturer": "Samsung",
        "device_software_build": "AP4A.250105.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; SM-G970F Build/AP4A.250105.002)"
    },
    {
        "android_version": 15,
        "device_name": "24076RP19G",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 24076RP19G Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 14,
        "device_name": "V2417",
        "device_manufacturer": "Vivo",
        "device_software_build": "UP1A.231005.007_NONFC",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2417 Build/UP1A.231005.007_NONFC)"
    },
    {
        "android_version": 14,
        "device_name": "XQ-ES44",
        "device_manufacturer": "Sony",
        "device_software_build": "70.0.A.3.136",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; XQ-ES44 Build/70.0.A.3.136)"
    },
    {
        "android_version": 15,
        "device_name": "ELP-NX9",
        "device_manufacturer": "Honor",
        "device_software_build": "HONORELP-N39",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; ELP-NX9 Build/HONORELP-N39)"
    },
    {
        "android_version": 15,
        "device_name": "V2317",
        "device_manufacturer": "Vivo",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; V2317 Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 14,
        "device_name": "SH-M29",
        "device_manufacturer": "Sharp",
        "device_software_build": "S903L",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SH-M29 Build/S903L)"
    },
    {
        "android_version": 15,
        "device_name": "RMX5000",
        "device_manufacturer": "Realme",
        "device_software_build": "UKQ1.231108.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; RMX5000 Build/UKQ1.231108.001)"
    },
    {
        "android_version": 15,
        "device_name": "2311DRN14I",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 2311DRN14I Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 4a",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250105.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 4a Build/AP4A.250105.002)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 6 Pro",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250105.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 6 Pro Build/AP4A.250105.002)"
    },
    {
        "android_version": 15,
        "device_name": "moto g15",
        "device_manufacturer": "Motorola",
        "device_software_build": "VVTA35.51-28-15",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; moto g15 Build/VVTA35.51-28-15)"
    },
    {
        "android_version": 14,
        "device_name": "moto g stylus 5G - 2024",
        "device_manufacturer": "Motorola",
        "device_software_build": "U2UBS34.44-57-10",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g stylus 5G - 2024 Build/U2UBS34.44-57-10)"
    },
    {
        "android_version": 14,
        "device_name": "SHG14",
        "device_manufacturer": "Sharp",
        "device_software_build": "S903L",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SHG14 Build/S903L)"
    },
    {
        "android_version": 15,
        "device_name": "SH-M26",
        "device_manufacturer": "Sharp",
        "device_software_build": "SB15N",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; SH-M26 Build/SB15N)"
    },
    {
        "android_version": 15,
        "device_name": "V2314",
        "device_manufacturer": "Vivo",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; V2314 Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 14,
        "device_name": "A208SH",
        "device_manufacturer": "Sony",
        "device_software_build": "SB150",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; A208SH Build/SB150)"
    },
    {
        "android_version": 14,
        "device_name": "2411DRN47I",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "UKQ1.240523.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; 2411DRN47I Build/UKQ1.240523.001)"
    },
    {
        "android_version": 15,
        "device_name": "V2405A",
        "device_manufacturer": "Vivo",
        "device_software_build": "AP3A.240905.015.A1_V000L1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; V2405A Build/AP3A.240905.015.A1_V000L1)"
    },
    {
        "android_version": 14,
        "device_name": "24090RA29I",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; 24090RA29I Build/UP1A.231005.007)"
    },
    {
        "android_version": 15,
        "device_name": "CPH2653",
        "device_manufacturer": "Oppo",
        "device_software_build": "AP3A.240617.008",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; CPH2653 Build/AP3A.240617.008)"
    },
    {
        "android_version": 15,
        "device_name": "SO-51E",
        "device_manufacturer": "Sony",
        "device_software_build": "69.1.A.2.115",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; SO-51E Build/69.1.A.2.115)"
    },
    {
        "android_version": 14,
        "device_name": "moto g75 5G",
        "device_manufacturer": "Motorola",
        "device_software_build": "U4UQ34.50-43-2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g75 5G Build/U4UQ34.50-43-2)"
    },
    {
        "android_version": 15,
        "device_name": "2404APC5FG",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 2404APC5FG Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 14,
        "device_name": "23043RP34C",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "UKQ1.230917.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; 23043RP34C Build/UKQ1.230917.001)"
    },
    {
        "android_version": 15,
        "device_name": "RMX3800",
        "device_manufacturer": "Realme",
        "device_software_build": "UKQ1.231108.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; RMX3800 Build/UKQ1.231108.001)"
    },
    {
        "android_version": 15,
        "device_name": "XQ-DE72",
        "device_manufacturer": "Sony",
        "device_software_build": "67.2.A.2.41",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; XQ-DE72 Build/67.2.A.2.41)"
    },
    {
        "android_version": 15,
        "device_name": "SM-G970F",
        "device_manufacturer": "Samsung",
        "device_software_build": "AP3A.241105.008",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; SM-G970F Build/AP3A.241105.008)"
    },
    {
        "android_version": 15,
        "device_name": "V2339",
        "device_manufacturer": "Vivo",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; V2339 Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 14,
        "device_name": "moto g64 5G",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TDS34.100-46-1-2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g64 5G Build/U1TDS34.100-46-1-2)"
    },
    {
        "android_version": 15,
        "device_name": "V2318",
        "device_manufacturer": "Vivo",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; V2318 Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 14,
        "device_name": "SH-54D",
        "device_manufacturer": "Sharp",
        "device_software_build": "SA182",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SH-54D Build/SA182)"
    },
    {
        "android_version": 15,
        "device_name": "CPH2519",
        "device_manufacturer": "Oppo",
        "device_software_build": "AP3A.240617.008",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; CPH2519 Build/AP3A.240617.008)"
    },
    {
        "android_version": 15,
        "device_name": "CPH2645",
        "device_manufacturer": "Oppo",
        "device_software_build": "UKQ1.231108.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; CPH2645 Build/UKQ1.231108.001)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 6",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250105.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 6 Build/AP4A.250105.002)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel Fold",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250105.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel Fold Build/AP4A.250105.002)"
    },
    {
        "android_version": 15,
        "device_name": "ONEPLUS A5010",
        "device_manufacturer": "OnePlus",
        "device_software_build": "AP4A.250105.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; ONEPLUS A5010 Build/AP4A.250105.002)"
    },
    {
        "android_version": 14,
        "device_name": "23077RABDC",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "UKQ1.230917.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; 23077RABDC Build/UKQ1.230917.001)"
    },
    {
        "android_version": 14,
        "device_name": "SO-53C",
        "device_manufacturer": "Sony",
        "device_software_build": "63.2.B.1.127",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SO-53C Build/63.2.B.1.127)"
    },
    {
        "android_version": 14,
        "device_name": "HD1901",
        "device_manufacturer": "OnePlus",
        "device_software_build": "AP2A.240705.005",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; HD1901 Build/AP2A.240705.005)"
    },
    {
        "android_version": 14,
        "device_name": "motorola razr 2022",
        "device_manufacturer": "Motorola",
        "device_software_build": "U2SLS34.1-42-14-5",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; motorola razr 2022 Build/U2SLS34.1-42-14-5)"
    },
    {
        "android_version": 15,
        "device_name": "XQ-EC54",
        "device_manufacturer": "Sony",
        "device_software_build": "69.1.A.2.100",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; XQ-EC54 Build/69.1.A.2.100)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 9",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.241205.013.C1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 9 Build/AP4A.241205.013.C1)"
    },
    {
        "android_version": 14,
        "device_name": "motorola razr 50 ultra",
        "device_manufacturer": "Motorola",
        "device_software_build": "U3UXS34.56-124-1-1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; motorola razr 50 ultra Build/U3UXS34.56-124-1-1)"
    },
    {
        "android_version": 14,
        "device_name": "Power Armor 18T",
        "device_manufacturer": "Ulefone",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Power Armor 18T Build/UP1A.231005.007)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 7 Pro",
        "device_manufacturer": "Google",
        "device_software_build": "BP11.241121.013",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 7 Pro Build/BP11.241121.013)"
    },
    {
        "android_version": 14,
        "device_name": "ThinkPhone by motorola",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TBS34.54-24-1-11-4-13",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; ThinkPhone by motorola Build/U1TBS34.54-24-1-11-4-13)"
    },
    {
        "android_version": 15,
        "device_name": "moto g power 5G - 2024",
        "device_manufacturer": "Motorola",
        "device_software_build": "V1UD35H.26-14-2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; moto g power 5G - 2024 Build/V1UD35H.26-14-2)"
    },
    {
        "android_version": 15,
        "device_name": "2405CRPFDL",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AQ3A.240912.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 2405CRPFDL Build/AQ3A.240912.001)"
    },
    {
        "android_version": 15,
        "device_name": "23076RN8DY",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AQ3A.240912.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 23076RN8DY Build/AQ3A.240912.001)"
    },
    {
        "android_version": 14,
        "device_name": "moto g53s 5G",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TPJ34.29-83-6-3",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g53s 5G Build/U1TPJ34.29-83-6-3)"
    },
    {
        "android_version": 14,
        "device_name": "Mi 9 SE",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AP2A.240905.003",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Mi 9 SE Build/AP2A.240905.003)"
    },
    {
        "android_version": 15,
        "device_name": "Xperia 5 II",
        "device_manufacturer": "Sony",
        "device_software_build": "AP4A.250105.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Xperia 5 II Build/AP4A.250105.002)"
    },
    {
        "android_version": 15,
        "device_name": "CPH2663",
        "device_manufacturer": "Oppo",
        "device_software_build": "UKQ1.231108.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; CPH2663 Build/UKQ1.231108.001)"
    },
    {
        "android_version": 14,
        "device_name": "moto g75 5G",
        "device_manufacturer": "Motorola",
        "device_software_build": "U4UQS34.50-29-2-1-1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g75 5G Build/U4UQS34.50-29-2-1-1)"
    },
    {
        "android_version": 14,
        "device_name": "24094RAD4G",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; 24094RAD4G Build/UP1A.231005.007)"
    },
    {
        "android_version": 14,
        "device_name": "24116RACCG",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; 24116RACCG Build/UP1A.231005.007)"
    },
    {
        "android_version": 14,
        "device_name": "SO-51D",
        "device_manufacturer": "Sony",
        "device_software_build": "67.1.B.2.215",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SO-51D Build/67.1.B.2.215)"
    },
    {
        "android_version": 14,
        "device_name": "RMX3770",
        "device_manufacturer": "Realme",
        "device_software_build": "UKQ1.230924.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; RMX3770 Build/UKQ1.230924.001)"
    },
    {
        "android_version": 14,
        "device_name": "A401SO",
        "device_manufacturer": "Sony",
        "device_software_build": "69.0.D.2.46",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; A401SO Build/69.0.D.2.46)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 9 Pro Fold",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250105.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 9 Pro Fold Build/AP4A.250105.002)"
    },
    {
        "android_version": 15,
        "device_name": "motorola razr 40 ultra",
        "device_manufacturer": "Motorola",
        "device_software_build": "V1TZ35H.41-21-3",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; motorola razr 40 ultra Build/V1TZ35H.41-21-3)"
    },
    {
        "android_version": 15,
        "device_name": "V2413",
        "device_manufacturer": "Vivo",
        "device_software_build": "AP3A.240905.015.A2_V000L1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; V2413 Build/AP3A.240905.015.A2_V000L1)"
    },
    {
        "android_version": 15,
        "device_name": "Xperia 5 II",
        "device_manufacturer": "Sony",
        "device_software_build": "AP4A.241205.013",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Xperia 5 II Build/AP4A.241205.013)"
    },
    {
        "android_version": 15,
        "device_name": "CPH2525",
        "device_manufacturer": "Oppo",
        "device_software_build": "AP3A.240617.008",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; CPH2525 Build/AP3A.240617.008)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 6a",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250105.002.A1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 6a Build/AP4A.250105.002.A1)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 9 Pro XL",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250105.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 9 Pro XL Build/AP4A.250105.002)"
    },
    {
        "android_version": 15,
        "device_name": "24074RPD2G",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AQ3A.240912.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 24074RPD2G Build/AQ3A.240912.001)"
    },
    {
        "android_version": 14,
        "device_name": "moto g power 5G - 2023",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TOS34.1-157-5-2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g power 5G - 2023 Build/U1TOS34.1-157-5-2)"
    },
    {
        "android_version": 14,
        "device_name": "moto g play - 2024",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TFS34.100-35-4-4",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g play - 2024 Build/U1TFS34.100-35-4-4)"
    },
    {
        "android_version": 14,
        "device_name": "moto g 5G - 2024",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1UFNS34.41-98-3-11",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g 5G - 2024 Build/U1UFNS34.41-98-3-11)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 7 Pro",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250105.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 7 Pro Build/AP4A.250105.002)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 9",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250105.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 9 Build/AP4A.250105.002)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 8 Pro",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250105.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 8 Pro Build/AP4A.250105.002)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 6a",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250105.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 6a Build/AP4A.250105.002)"
    },
    {
        "android_version": 14,
        "device_name": "moto g 5G - 2023",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TPNS34.26-48-2-2-15",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g 5G - 2023 Build/U1TPNS34.26-48-2-2-15)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 6 Pro",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250105.002.A1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 6 Pro Build/AP4A.250105.002.A1)"
    },
    {
        "android_version": 15,
        "device_name": "V2341",
        "device_manufacturer": "Vivo",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; V2341 Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 15,
        "device_name": "CPH2603",
        "device_manufacturer": "Oppo",
        "device_software_build": "AP3A.240617.008",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; CPH2603 Build/AP3A.240617.008)"
    },
    {
        "android_version": 14,
        "device_name": "V2419",
        "device_manufacturer": "Vivo",
        "device_software_build": "UP1A.231005.007_NN",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2419 Build/UP1A.231005.007_NN)"
    },
    {
        "android_version": 15,
        "device_name": "CPH2619",
        "device_manufacturer": "Oppo",
        "device_software_build": "AP3A.240617.008",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; CPH2619 Build/AP3A.240617.008)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 7",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250105.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 7 Build/AP4A.250105.002)"
    },
    {
        "android_version": 14,
        "device_name": "motorola razr 50",
        "device_manufacturer": "Motorola",
        "device_software_build": "U3UC34.63-105-15",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; motorola razr 50 Build/U3UC34.63-105-15)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 8",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250105.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 8 Build/AP4A.250105.002)"
    },
    {
        "android_version": 14,
        "device_name": "SM-L315U",
        "device_manufacturer": "Samsung",
        "device_software_build": "AW2E.240318.016",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SM-L315U Build/AW2E.240318.016)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 9 Pro",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.250105.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 9 Pro Build/AP4A.250105.002)"
    },
    {
        "android_version": 14,
        "device_name": "24117RN76E",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; 24117RN76E Build/UP1A.231005.007)"
    },
    {
        "android_version": 14,
        "device_name": "moto e14",
        "device_manufacturer": "Motorola",
        "device_software_build": "ULB34.66-108",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto e14 Build/ULB34.66-108)"
    },
    {
        "android_version": 14,
        "device_name": "SH-52D",
        "device_manufacturer": "Sharp",
        "device_software_build": "SA190",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SH-52D Build/SA190)"
    },
    {
        "android_version": 14,
        "device_name": "moto g34 5G",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1UGS34.23-82-4-5",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g34 5G Build/U1UGS34.23-82-4-5)"
    },
    {
        "android_version": 14,
        "device_name": "BV4800 Pro",
        "device_manufacturer": "Blackview",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; BV4800 Pro Build/UP1A.231005.007)"
    },
    {
        "android_version": 14,
        "device_name": "Pixel 3a",
        "device_manufacturer": "Google",
        "device_software_build": "AP2A.240905.003",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Pixel 3a Build/AP2A.240905.003)"
    },
    {
        "android_version": 15,
        "device_name": "23108RN04Y",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 23108RN04Y Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 14,
        "device_name": "moto g53 5G",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TPS34.29-83-6-5",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g53 5G Build/U1TPS34.29-83-6-5)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 8",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.241205.013.C1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 8 Build/AP4A.241205.013.C1)"
    },
    {
        "android_version": 14,
        "device_name": "SH-M27",
        "device_manufacturer": "Sharp",
        "device_software_build": "SA290",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SH-M27 Build/SA290)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel Fold",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.241205.013",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel Fold Build/AP4A.241205.013)"
    },
    {
        "android_version": 15,
        "device_name": "CPH2689",
        "device_manufacturer": "Oppo",
        "device_software_build": "UKQ1.231108.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; CPH2689 Build/UKQ1.231108.001)"
    },
    {
        "android_version": 14,
        "device_name": "NX725J",
        "device_manufacturer": "Nubia",
        "device_software_build": "UKQ1.230917.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; NX725J Build/UKQ1.230917.001)"
    },
    {
        "android_version": 15,
        "device_name": "CPH2621",
        "device_manufacturer": "Oppo",
        "device_software_build": "AP3A.240617.008",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; CPH2621 Build/AP3A.240617.008)"
    },
    {
        "android_version": 14,
        "device_name": "SH-52E",
        "device_manufacturer": "Sharp",
        "device_software_build": "S5223",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SH-52E Build/S5223)"
    },
    {
        "android_version": 15,
        "device_name": "CPH2629",
        "device_manufacturer": "Oppo",
        "device_software_build": "AP3A.240617.008",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; CPH2629 Build/AP3A.240617.008)"
    },
    {
        "android_version": 14,
        "device_name": "moto g53 5G",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TPS34.29-83-7-3-2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g53 5G Build/U1TPS34.29-83-7-3-2)"
    },
    {
        "android_version": 14,
        "device_name": "BV8100",
        "device_manufacturer": "Blackview",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; BV8100 Build/UP1A.231005.007)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 7a",
        "device_manufacturer": "Google",
        "device_software_build": "BP11.241121.010",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 7a Build/BP11.241121.010)"
    },
    {
        "android_version": 14,
        "device_name": "moto g play - 2024",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TFS34.100-35-2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g play - 2024 Build/U1TFS34.100-35-2)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 6a",
        "device_manufacturer": "Google",
        "device_software_build": "BP11.241121.010",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 6a Build/BP11.241121.010)"
    },
    {
        "android_version": 14,
        "device_name": "SM-A165M",
        "device_manufacturer": "Samsung",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SM-A165M Build/UP1A.231005.007)"
    },
    {
        "android_version": 15,
        "device_name": "23122PCD1G",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AQ3A.240912.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 23122PCD1G Build/AQ3A.240912.001)"
    },
    {
        "android_version": 15,
        "device_name": "2311DRK48G",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 2311DRK48G Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 15,
        "device_name": "V2348",
        "device_manufacturer": "Vivo",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; V2348 Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 14,
        "device_name": "SM-A1660",
        "device_manufacturer": "Samsung",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SM-A1660 Build/UP1A.231005.007)"
    },
    {
        "android_version": 14,
        "device_name": "SOG13",
        "device_manufacturer": "Sony",
        "device_software_build": "69.0.C.2.42",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SOG13 Build/69.0.C.2.42)"
    },
    {
        "android_version": 15,
        "device_name": "XQ-EC54",
        "device_manufacturer": "Sony",
        "device_software_build": "69.1.A.2.78",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; XQ-EC54 Build/69.1.A.2.78)"
    },
    {
        "android_version": 14,
        "device_name": "V2424",
        "device_manufacturer": "Vivo",
        "device_software_build": "UP1A.231005.007_NN",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2424 Build/UP1A.231005.007_NN)"
    },
    {
        "android_version": 14,
        "device_name": "moto g73 5G",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TNS34.82-12-7-8",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g73 5G Build/U1TNS34.82-12-7-8)"
    },
    {
        "android_version": 15,
        "device_name": "23021RAAEG",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AQ3A.240829.003",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 23021RAAEG Build/AQ3A.240829.003)"
    },
    {
        "android_version": 15,
        "device_name": "CPH2451",
        "device_manufacturer": "Oppo",
        "device_software_build": "TP1A.220905.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; CPH2451 Build/TP1A.220905.001)"
    },
    {
        "android_version": 15,
        "device_name": "V2403",
        "device_manufacturer": "Vivo",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; V2403 Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 14,
        "device_name": "SM-E055F",
        "device_manufacturer": "Samsung",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SM-E055F Build/UP1A.231005.007)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 7",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.241205.013.C1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 7 Build/AP4A.241205.013.C1)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 7",
        "device_manufacturer": "Google",
        "device_software_build": "BP11.241121.010",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 7 Build/BP11.241121.010)"
    },
    {
        "android_version": 14,
        "device_name": "A202SH",
        "device_manufacturer": "Sony",
        "device_software_build": "SA180",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; A202SH Build/SA180)"
    },
    {
        "android_version": 14,
        "device_name": "moto g55 5G",
        "device_manufacturer": "Motorola",
        "device_software_build": "U3UT34.44-73-4",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g55 5G Build/U3UT34.44-73-4)"
    },
    {
        "android_version": 14,
        "device_name": "motorola razr 2024",
        "device_manufacturer": "Motorola",
        "device_software_build": "U3UCS34.63-88-12-1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; motorola razr 2024 Build/U3UCS34.63-88-12-1)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 9 Pro",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.241205.013.C1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 9 Pro Build/AP4A.241205.013.C1)"
    },
    {
        "android_version": 14,
        "device_name": "SM-G970F",
        "device_manufacturer": "Samsung",
        "device_software_build": "AP2A.240905.003",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SM-G970F Build/AP2A.240905.003)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 7",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.241205.013.B1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 7 Build/AP4A.241205.013.B1)"
    },
    {
        "android_version": 15,
        "device_name": "CPH2665",
        "device_manufacturer": "Oppo",
        "device_software_build": "AP3A.240617.008",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; CPH2665 Build/AP3A.240617.008)"
    },
    {
        "android_version": 14,
        "device_name": "SHG11",
        "device_manufacturer": "Sharp",
        "device_software_build": "SA181",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SHG11 Build/SA181)"
    },
    {
        "android_version": 14,
        "device_name": "SH-51E",
        "device_manufacturer": "Sharp",
        "device_software_build": "SA170",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SH-51E Build/SA170)"
    },
    {
        "android_version": 14,
        "device_name": "FNE-AN00",
        "device_manufacturer": "Honor",
        "device_software_build": "HONORFNE-AN00",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; FNE-AN00 Build/HONORFNE-AN00)"
    },
    {
        "android_version": 15,
        "device_name": "BVL-N49",
        "device_manufacturer": "Honor",
        "device_software_build": "HONORBVL-N49",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; BVL-N49 Build/HONORBVL-N49)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 7a",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.241205.013.C1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 7a Build/AP4A.241205.013.C1)"
    },
    {
        "android_version": 14,
        "device_name": "A301SH",
        "device_manufacturer": "Sony",
        "device_software_build": "SC416",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; A301SH Build/SC416)"
    },
    {
        "android_version": 14,
        "device_name": "SM-S721N",
        "device_manufacturer": "Samsung",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SM-S721N Build/UP1A.231005.007)"
    },
    {
        "android_version": 15,
        "device_name": "V2218",
        "device_manufacturer": "Vivo",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; V2218 Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 14,
        "device_name": "TECNO KL7",
        "device_manufacturer": "Tecno",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; TECNO KL7 Build/UP1A.231005.007)"
    },
    {
        "android_version": 14,
        "device_name": "SOG11",
        "device_manufacturer": "Sony",
        "device_software_build": "68.1.C.2.240",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SOG11 Build/68.1.C.2.240)"
    },
    {
        "android_version": 15,
        "device_name": "23106RN0DA",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 23106RN0DA Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 15,
        "device_name": "CPH2625",
        "device_manufacturer": "Oppo",
        "device_software_build": "AP3A.240617.008",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; CPH2625 Build/AP3A.240617.008)"
    },
    {
        "android_version": 15,
        "device_name": "CPH2637",
        "device_manufacturer": "Oppo",
        "device_software_build": "AP3A.240617.008",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; CPH2637 Build/AP3A.240617.008)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 7 Pro",
        "device_manufacturer": "Google",
        "device_software_build": "BP11.241121.010",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 7 Pro Build/BP11.241121.010)"
    },
    {
        "android_version": 14,
        "device_name": "HTC U24 pro",
        "device_manufacturer": "HTC",
        "device_software_build": "1.17.709.1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; HTC U24 pro Build/1.17.709.1)"
    },
    {
        "android_version": 15,
        "device_name": "23053RN02Y",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 23053RN02Y Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 15,
        "device_name": "CPH2659",
        "device_manufacturer": "Oppo",
        "device_software_build": "AP3A.240617.008",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; CPH2659 Build/AP3A.240617.008)"
    },
    {
        "android_version": 14,
        "device_name": "NDL-L09",
        "device_manufacturer": "Honor",
        "device_software_build": "HONORNDL-L09",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; NDL-L09 Build/HONORNDL-L09)"
    },
    {
        "android_version": 15,
        "device_name": "RMX3999",
        "device_manufacturer": "Realme",
        "device_software_build": "AP3A.240617.008",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; RMX3999 Build/AP3A.240617.008)"
    },
    {
        "android_version": 14,
        "device_name": "motorola razr 50",
        "device_manufacturer": "Motorola",
        "device_software_build": "U3UCS34.63-88-18-1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; motorola razr 50 Build/U3UCS34.63-88-18-1)"
    },
    {
        "android_version": 15,
        "device_name": "CPH2639",
        "device_manufacturer": "Oppo",
        "device_software_build": "AP3A.240617.008",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; CPH2639 Build/AP3A.240617.008)"
    },
    {
        "android_version": 14,
        "device_name": "V2327A",
        "device_manufacturer": "Vivo",
        "device_software_build": "UP1A.231005.007) SP-engine/2.87.0 baiduboxapp/13.49.0.10 (Baidu; P1 14) dumedia/7.45.34.24",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2327A Build/UP1A.231005.007) SP-engine/2.87.0 baiduboxapp/13.49.0.10 (Baidu; P1 14) dumedia/7.45.34.24"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 7 Pro",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.241205.013.C1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 7 Pro Build/AP4A.241205.013.C1)"
    },
    {
        "android_version": 15,
        "device_name": "2410CRP4CC",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AQ3A.240801.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 2410CRP4CC Build/AQ3A.240801.002)"
    },
    {
        "android_version": 15,
        "device_name": "2310FPCA4G",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 2310FPCA4G Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 14,
        "device_name": "RMX3869",
        "device_manufacturer": "Realme",
        "device_software_build": "UKQ1.230924.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; RMX3869 Build/UKQ1.230924.001)"
    },
    {
        "android_version": 15,
        "device_name": "23076PC4BI",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AQ3A.240912.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 23076PC4BI Build/AQ3A.240912.001)"
    },
    {
        "android_version": 14,
        "device_name": "moto g64 5G",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TDS34.100-46-1-4",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g64 5G Build/U1TDS34.100-46-1-4)"
    },
    {
        "android_version": 15,
        "device_name": "23124RA7EO",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AQ3A.240829.003",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 23124RA7EO Build/AQ3A.240829.003)"
    },
    {
        "android_version": 14,
        "device_name": "moto g stylus 5G - 2023",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TGNS34.42-86-2-4-4",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g stylus 5G - 2023 Build/U1TGNS34.42-86-2-4-4)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 9",
        "device_manufacturer": "Google",
        "device_software_build": "BP11.241121.010",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 9 Build/BP11.241121.010)"
    },
    {
        "android_version": 15,
        "device_name": "FCP-N49",
        "device_manufacturer": "Honor",
        "device_software_build": "HONORFCP-N49",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; FCP-N49 Build/HONORFCP-N49)"
    },
    {
        "android_version": 15,
        "device_name": "CPH2583",
        "device_manufacturer": "Oppo",
        "device_software_build": "AP3A.240617.008",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; CPH2583 Build/AP3A.240617.008)"
    },
    {
        "android_version": 14,
        "device_name": "NDL-L03",
        "device_manufacturer": "Honor",
        "device_software_build": "HONORNDL-L03",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; NDL-L03 Build/HONORNDL-L03)"
    },
    {
        "android_version": 14,
        "device_name": "SM-M055F",
        "device_manufacturer": "Samsung",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SM-M055F Build/UP1A.231005.007)"
    },
    {
        "android_version": 14,
        "device_name": "Pixel 9 Pro XL",
        "device_manufacturer": "Google",
        "device_software_build": "AD1A.240530.030.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Pixel 9 Pro XL Build/AD1A.240530.030.A2)"
    },
    {
        "android_version": 14,
        "device_name": "JDY-LX3",
        "device_manufacturer": "Honor",
        "device_software_build": "HONORJDY-L13",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; JDY-LX3 Build/HONORJDY-L13)"
    },
    {
        "android_version": 14,
        "device_name": "BV6200 Pro",
        "device_manufacturer": "Blackview",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; BV6200 Pro Build/UP1A.231005.007)"
    },
    {
        "android_version": 14,
        "device_name": "moto g play - 2024",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TFS34.100-35-5-2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g play - 2024 Build/U1TFS34.100-35-5-2)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 8",
        "device_manufacturer": "Google",
        "device_software_build": "BP11.241025.006",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 8 Build/BP11.241025.006)"
    },
    {
        "android_version": 14,
        "device_name": "moto g stylus 5G - 2024",
        "device_manufacturer": "Motorola",
        "device_software_build": "U2UBS34.44-108-1-1-1-1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g stylus 5G - 2024 Build/U2UBS34.44-108-1-1-1-1)"
    },
    {
        "android_version": 15,
        "device_name": "Pixel 8 Pro",
        "device_manufacturer": "Google",
        "device_software_build": "AP4A.241205.013.C1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Pixel 8 Pro Build/AP4A.241205.013.C1)"
    },
    {
        "android_version": 14,
        "device_name": "Redmi Note 8 Pro",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "UQ1A.240205.004",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Redmi Note 8 Pro Build/UQ1A.240205.004)"
    },
    {
        "android_version": 14,
        "device_name": "moto g35 5G",
        "device_manufacturer": "Motorola",
        "device_software_build": "UOA34.216-129-1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g35 5G Build/UOA34.216-129-1)"
    },
    {
        "android_version": 14,
        "device_name": "TECNO KL8",
        "device_manufacturer": "Tecno",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; TECNO KL8 Build/UP1A.231005.007)"
    },
    {
        "android_version": 15,
        "device_name": "G8142",
        "device_manufacturer": "Asus",
        "device_software_build": "AP3A.241105.008",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; G8142 Build/AP3A.241105.008)"
    },
    {
        "android_version": 14,
        "device_name": "SO-51E",
        "device_manufacturer": "Sony",
        "device_software_build": "69.0.B.2.56",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SO-51E Build/69.0.B.2.56)"
    },
    {
        "android_version": 14,
        "device_name": "SM-A166P",
        "device_manufacturer": "Samsung",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SM-A166P Build/UP1A.231005.007)"
    },
    {
        "android_version": 14,
        "device_name": "motorola razr 50",
        "device_manufacturer": "Motorola",
        "device_software_build": "U3UC34.63-88-18",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; motorola razr 50 Build/U3UC34.63-88-18)"
    },
    {
        "android_version": 14,
        "device_name": "moto g stylus 5G - 2023",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TGNS34.42-86-4-5",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g stylus 5G - 2023 Build/U1TGNS34.42-86-4-5)"
    },
    {
        "android_version": 14,
        "device_name": "moto g75 5G",
        "device_manufacturer": "Motorola",
        "device_software_build": "U4UQS34.50-29-4-4",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g75 5G Build/U4UQS34.50-29-4-4)"
    },
    {
        "android_version": 14,
        "device_name": "IN2010",
        "device_manufacturer": "OnePlus",
        "device_software_build": "AP2A.240905.003",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; IN2010 Build/AP2A.240905.003)"
    },
    {
        "android_version": 14,
        "device_name": "RMX3951",
        "device_manufacturer": "Realme",
        "device_software_build": "UKQ1.231108.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; RMX3951 Build/UKQ1.231108.001)"
    },
    {
        "android_version": 15,
        "device_name": "NX733J",
        "device_manufacturer": "Nubia",
        "device_software_build": "AQ3A.240812.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; NX733J Build/AQ3A.240812.002)"
    },
    {
        "android_version": 14,
        "device_name": "SH-M24",
        "device_manufacturer": "Sharp",
        "device_software_build": "SB130",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SH-M24 Build/SB130)"
    },
    {
        "android_version": 14,
        "device_name": "motorola razr plus 2023",
        "device_manufacturer": "Motorola",
        "device_software_build": "U3TZS34.2-65-3-6",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; motorola razr plus 2023 Build/U3TZS34.2-65-3-6)"
    },
    {
        "android_version": 15,
        "device_name": "2211133C",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AQ3A.240912.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 2211133C Build/AQ3A.240912.001)"
    },
    {
        "android_version": 14,
        "device_name": "Blade GT",
        "device_manufacturer": "ZTE",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Blade GT Build/UP1A.231005.007)"
    },
    {
        "android_version": 15,
        "device_name": "V2309",
        "device_manufacturer": "Vivo",
        "device_software_build": "AP3A.240905.015.A1_IN",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; V2309 Build/AP3A.240905.015.A1_IN)"
    },
    {
        "android_version": 15,
        "device_name": "V2170A",
        "device_manufacturer": "Vivo",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; V2170A Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 15,
        "device_name": "V2303",
        "device_manufacturer": "Vivo",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; V2303 Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 15,
        "device_name": "XQ-DQ54",
        "device_manufacturer": "Sony",
        "device_software_build": "67.2.A.2.41",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; XQ-DQ54 Build/67.2.A.2.41)"
    },
    {
        "android_version": 15,
        "device_name": "SM-S938B",
        "device_manufacturer": "Samsung",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; SM-S938B Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 15,
        "device_name": "24031PN0DC",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AQ3A.240627.003",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 24031PN0DC Build/AQ3A.240627.003)"
    },
    {
        "android_version": 14,
        "device_name": "XQ-CC54",
        "device_manufacturer": "Sony",
        "device_software_build": "65.2.A.2.224",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; XQ-CC54 Build/65.2.A.2.224)"
    },
    {
        "android_version": 14,
        "device_name": "LE2123",
        "device_manufacturer": "OnePlus",
        "device_software_build": "UKQ1.240723.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; LE2123 Build/UKQ1.240723.001)"
    },
    {
        "android_version": 15,
        "device_name": "A001",
        "device_manufacturer": "OnePlus",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; A001 Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 14,
        "device_name": "V2118A",
        "device_manufacturer": "Vivo",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2118A Build/UP1A.231005.007)"
    },
    {
        "android_version": 14,
        "device_name": "Infinix X6881",
        "device_manufacturer": "Infinix",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Infinix X6881 Build/UP1A.231005.007)"
    },
    {
        "android_version": 14,
        "device_name": "PGT110",
        "device_manufacturer": "Tecno",
        "device_software_build": "UKQ1.230924.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; PGT110 Build/UKQ1.230924.001)"
    },
    {
        "android_version": 15,
        "device_name": "2312FPCA6G",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 2312FPCA6G Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 15,
        "device_name": "HMD Pulse Pro",
        "device_manufacturer": "HMD Global",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; HMD Pulse Pro Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 15,
        "device_name": "Infinix X6835B",
        "device_manufacturer": "Infinix",
        "device_software_build": "AP4A.250105.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Infinix X6835B Build/AP4A.250105.002)"
    },
    {
        "android_version": 15,
        "device_name": "ELI-NX9",
        "device_manufacturer": "Honor",
        "device_software_build": "HONORELI-N39",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; ELI-NX9 Build/HONORELI-N39)"
    },
    {
        "android_version": 15,
        "device_name": "MI 8",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AP4A.250105.002",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; MI 8 Build/AP4A.250105.002)"
    },
    {
        "android_version": 14,
        "device_name": "BRP-NX1M",
        "device_manufacturer": "Honor",
        "device_software_build": "HONORBRP-N21M",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; BRP-NX1M Build/HONORBRP-N21M)"
    },
    {
        "android_version": 14,
        "device_name": "XQ-CQ44",
        "device_manufacturer": "Sony",
        "device_software_build": "64.2.A.2.224",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; XQ-CQ44 Build/64.2.A.2.224)"
    },
    {
        "android_version": 14,
        "device_name": "S41 Max",
        "device_manufacturer": "Doogee",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; S41 Max Build/UP1A.231005.007)"
    },
    {
        "android_version": 14,
        "device_name": "itel A669W",
        "device_manufacturer": "Itel",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; itel A669W Build/UP1A.231005.007)"
    },
    {
        "android_version": 15,
        "device_name": "2211133G",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AQ3A.240912.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 2211133G Build/AQ3A.240912.001)"
    },
    {
        "android_version": 15,
        "device_name": "MI 8",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AP4A.241205.013",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; MI 8 Build/AP4A.241205.013)"
    },
    {
        "android_version": 15,
        "device_name": "PTP-AN10",
        "device_manufacturer": "Honor",
        "device_software_build": "HONORPTP-AN10",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; PTP-AN10 Build/HONORPTP-AN10)"
    },
    {
        "android_version": 14,
        "device_name": "Mblu 21",
        "device_manufacturer": "Meizu",
        "device_software_build": "U01005",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Mblu 21 Build/U01005)"
    },
    {
        "android_version": 14,
        "device_name": "SM-A166U",
        "device_manufacturer": "Samsung",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SM-A166U Build/UP1A.231005.007)"
    },
    {
        "android_version": 15,
        "device_name": "23021RAA2Y",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AQ3A.240829.003",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 23021RAA2Y Build/AQ3A.240829.003)"
    },
    {
        "android_version": 14,
        "device_name": "V2185A",
        "device_manufacturer": "Vivo",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2185A Build/UP1A.231005.007)"
    },
    {
        "android_version": 14,
        "device_name": "moto g53y 5G",
        "device_manufacturer": "Motorola",
        "device_software_build": "U1TPJ34.29-83-6-3",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g53y 5G Build/U1TPJ34.29-83-6-3)"
    },
    {
        "android_version": 14,
        "device_name": "SH-R80",
        "device_manufacturer": "Sharp",
        "device_software_build": "SA190",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SH-R80 Build/SA190)"
    },
    {
        "android_version": 14,
        "device_name": "24040RA98R",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; 24040RA98R Build/UP1A.231005.007)"
    },
    {
        "android_version": 14,
        "device_name": "V2201",
        "device_manufacturer": "Vivo",
        "device_software_build": "UP1A.231005.007_SC",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2201 Build/UP1A.231005.007_SC)"
    },
    {
        "android_version": 15,
        "device_name": "23028RA60L",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AQ3A.240829.003",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 23028RA60L Build/AQ3A.240829.003)"
    },
    {
        "android_version": 14,
        "device_name": "Infinix X6720B",
        "device_manufacturer": "Infinix",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Infinix X6720B Build/UP1A.231005.007)"
    },
    {
        "android_version": 15,
        "device_name": "Xiaomi 13",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AP3A.241105.008",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; Xiaomi 13 Build/AP3A.241105.008)"
    },
    {
        "android_version": 15,
        "device_name": "24049RN28L",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 24049RN28L Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 14,
        "device_name": "moto g24 power",
        "device_manufacturer": "Motorola",
        "device_software_build": "UTA34.82-97",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g24 power Build/UTA34.82-97)"
    },
    {
        "android_version": 14,
        "device_name": "moto g04",
        "device_manufacturer": "Motorola",
        "device_software_build": "ULA34.89-177",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g04 Build/ULA34.89-177)"
    },
    {
        "android_version": 15,
        "device_name": "CPH2449",
        "device_manufacturer": "Oppo",
        "device_software_build": "TP1A.220905.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; CPH2449 Build/TP1A.220905.001)"
    },
    {
        "android_version": 14,
        "device_name": "U572AA",
        "device_manufacturer": "Alcatel",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; U572AA Build/UP1A.231005.007)"
    },
    {
        "android_version": 14,
        "device_name": "Infinix X6880",
        "device_manufacturer": "Infinix",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; Infinix X6880 Build/UP1A.231005.007)"
    },
    {
        "android_version": 14,
        "device_name": "V2205",
        "device_manufacturer": "Vivo",
        "device_software_build": "UP1A.231005.007); appId=com.zenofm.player; appVersion=6.0.7(600751",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; V2205 Build/UP1A.231005.007); appId=com.zenofm.player; appVersion=6.0.7(600751)"
    },
    {
        "android_version": 14,
        "device_name": "moto g24",
        "device_manufacturer": "Motorola",
        "device_software_build": "UTA34.82-97",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g24 Build/UTA34.82-97)"
    },
    {
        "android_version": 15,
        "device_name": "2312DRA50G",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AQ3A.240912.001",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 2312DRA50G Build/AQ3A.240912.001)"
    },
    {
        "android_version": 14,
        "device_name": "moto g24 power",
        "device_manufacturer": "Motorola",
        "device_software_build": "UTAS34.82-28-1-1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g24 power Build/UTAS34.82-28-1-1)"
    },
    {
        "android_version": 14,
        "device_name": "moto g04s",
        "device_manufacturer": "Motorola",
        "device_software_build": "ULA34.89-177",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g04s Build/ULA34.89-177)"
    },
    {
        "android_version": 14,
        "device_name": "MI 9",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AP2A.240905.003.F1",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; MI 9 Build/AP2A.240905.003.F1)"
    },
    {
        "android_version": 14,
        "device_name": "A402SH",
        "device_manufacturer": "Sharp",
        "device_software_build": "S5223",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; A402SH Build/S5223)"
    },
    {
        "android_version": 15,
        "device_name": "SM-S928U1",
        "device_manufacturer": "Samsung",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; SM-S928U1 Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 14,
        "device_name": "S41 Plus",
        "device_manufacturer": "Doogee",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; S41 Plus Build/UP1A.231005.007)"
    },
    {
        "android_version": 14,
        "device_name": "itel A671LC",
        "device_manufacturer": "Itel",
        "device_software_build": "UP1A.231005.007",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; itel A671LC Build/UP1A.231005.007)"
    },
    {
        "android_version": 15,
        "device_name": "CPH2607",
        "device_manufacturer": "Oppo",
        "device_software_build": "SP1A.210812.016",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; CPH2607 Build/SP1A.210812.016)"
    },
    {
        "android_version": 14,
        "device_name": "SO-54C",
        "device_manufacturer": "Sony",
        "device_software_build": "64.2.C.2.216",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; SO-54C Build/64.2.C.2.216)"
    },
    {
        "android_version": 15,
        "device_name": "23053RN02L",
        "device_manufacturer": "Xiaomi",
        "device_software_build": "AP3A.240905.015.A2",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 15; 23053RN02L Build/AP3A.240905.015.A2)"
    },
    {
        "android_version": 14,
        "device_name": "moto g14",
        "device_manufacturer": "Motorola",
        "device_software_build": "UTLB34.102-62",
        "dalvik_user_agent": "Dalvik/2.1.0 (Linux; U; Android 14; moto g14 Build/UTLB34.102-62)"
    }
]
