# FireBased

A based implementation of the Firebase API. This project is a partial wrapper around the Firebase API.

With just the teeniest bit of extra work, you can hook this up like
someone did in [Push-Server](https://github.com/lastrise/Push-Server) to a
REST API and have a full-fledged push notification server.

## Privacy Notice

Note that App developers CANNOT see the device you used to register with. 
Therefore, the device you register the FCM token with does not need to match the device you actually use the token with.
However, once you have associated an FCM token with a given device, at this point, the app developer CAN save that association.

## Note From The Creator

If you are using this, you are a developer. You know what you are doing.
I am not responsible for any misuse of this software.
I am not responsible for any bans or other actions taken against accounts using this software.

If you are hiring, e-mail `isaacikogan@gmail.com`. Let's chat :)! If not, say hi anwyways!

## Helpful Tips

There are only a few identifiers you need to make requests.
All of them can be found in the APK of the app you want to register firebase for:

- `google_api_key` e.g. "AIzaSyA1b2C3dE4f5G6H7I8J9K0LmNOpQrStUvWx"
- `google_app_id` e.g. "1:123456789012:android:abcdefghijklm1234567"
- `google_app_package` e.g. "com.example.app"
- `google_app_name` e.g. "api-project-123456789012"
- `google_android_cert` e.g. "12345678A1B2C3D4E5F6G7H8I9J0KLMNOPQRSTU"

For your convenience, here is a basic example script that can generate a GCM token:

```python
import asyncio

from FireBased.client.client import FireBasedClient
from FireBased.client.proto import CheckInRequestMessage, CheckInResponseMessage
from FireBased.client.schemas import RegisterInstallRequestBody, RegisterInstallRequestBodyJsonBody, RegisterGcmRequestBody, FirebaseInstallationRequestResponse, RegisterGcmRequestResponse
from FireBased.ext.synthetic_data import create_synthetic_check_in, create_mobile_user_agent

google_api_key = "AIzaSyA1b2C3dE4f5G6H7I8J9K0LmNOpQrStUvWx"  # Firebase API key
google_app_id = "1:123456789012:android:abcdefghijklm1234567"  # Firebase app ID
google_app_package = "com.example.app"  # Package name of the Android app
google_app_name = "api-project-123456789012"  # Firebase app name
google_android_cert = "12345678A1B2C3D4E5F6G7H8I9J0KLMNOPQRSTU"  # Sha-1 APK signing cert


async def generate_gcm_token() -> str:
    # Starts an HTTP client under the hood. Best to use in an async context manager for safety.
    async with FireBasedClient() as fb:
        # Create a synthetic check-in payload.
        # Note that according to ChatGPT, developers can't access the data you send here.
        # All they can really check is the Firebase ID, GCM token, and the Android ID.
        check_in_payload: CheckInRequestMessage = create_synthetic_check_in()
        check_in_response: CheckInResponseMessage = await fb.check_in(body=check_in_payload)

        # Create the installation registration payload
        register_install_payload: RegisterInstallRequestBody = RegisterInstallRequestBody(
            app_public_key=google_api_key,
            app_package=google_app_package,
            app_name=google_app_name,
            json_body=RegisterInstallRequestBodyJsonBody(appId=google_app_id),
            user_agent=create_mobile_user_agent(),
            app_cert=google_android_cert
        )

        # Register the installation
        install_data: FirebaseInstallationRequestResponse = await fb.register_install(
            body=register_install_payload
        )

        # Finally, register the GCM token using the data from the previous requests
        gcm_response: RegisterGcmRequestResponse = await fb.register_gcm(
            body=RegisterGcmRequestBody.from_models(
                install_request_body=register_install_payload,
                install_request_response=install_data,
                check_in_request_response=check_in_response
            )
        )

        return gcm_response.token


if __name__ == '__main__':
    gcm_token: str = asyncio.run(generate_gcm_token())
    print(f"Generated GCM token: {gcm_token}")
```

Latest pertinent data is found at `https://github.com/firebase/firebase-js-sdk`

## Contributors

* **Isaac Kogan** - *Creator, Primary Maintainer, and Reverse-Engineering* - [isaackogan](https://github.com/isaackogan)
* **Lastrise** - *Reverse-Engineering* - [lastrise](https://github.com/lastrise)

See also the full list of [contributors](https://github.com/isaackogan/Grindr/contributors) who have participated in
this project.

## License

This project is licensed under the GPL-3.0 License - see the [LICENSE](LICENSE) file for details.
