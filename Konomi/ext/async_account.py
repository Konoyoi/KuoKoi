from time import time

from .entities.userprofile import UserProfile
from .entities.general import (
    ApiResponse, Authenticate, ResetPassword, Wallet
    )


class AsyncAccount:
    """
    Account class for handling account related requests.
    """
    def __init__(self, session):
        self.session = session

    async def register(self, email: str, password: str, username: str, verificationCode: str) -> Authenticate:
        """
        `**register**` - Registers a new account.

        `**Parameters**`

        - `email` - The email of the account.

        - `password` - The password of the account.

        - `username` - The username of the account.

        - `verificationCode` - The verification code sent to the email.
        
        `**Example**`

        ```py
        from pymino import *

        bot = Bot()
        bot.request_security_validation(email=email)
        code = input("Enter the code you received: ")
        response = bot.register(email=email, password=password, username=username, verificationCode=code)
        print(response.json())
        ```
        """
        return Authenticate(await self.session.handler(
            method = "POST",
            url="/g/s/auth/register",
            data={
                "secret": f"0 {password}",
                "deviceID": self.session.generate.device_id(),
                "email": email,
                "clientType": 100,
                "nickname": username,
                "validationContext": {
                    "data": {"code": verificationCode}, "type": 1, "identity": email},
                "type": 1,
                "identity": email,
                "timestamp": int(time() * 1000)
                }))

    async def delete_request(self, email: str, password: str) -> ApiResponse:
        """
        `**delete_request**` - Sends a delete request to the account.

        `**Parameters**`

        - `email` - The email of the account.

        - `password` - The password of the account.
        
        `**Example**`

        ```py
        from pymino import *
        
        bot = Bot()
        bot.run(email=email, password=password)
        response = bot.delete_request(email=email, password=password)
        print(response)
        ```"""
        return ApiResponse(await self.session.handler(
            method = "POST",
            url="/g/s/account/delete-request",
            data={
                "secret": f"0 {password}",
                "deviceID": self.session.generate.device_id(),
                "email": email,
                "timestamp": int(time() * 1000)
            }))

    async def delete_request_cancel(self, email: str, password: str) -> ApiResponse:
        """
        `**delete_request_cancel**` - Cancels the delete request.

        `**Parameters**`

        - `email` - The email of the account.

        - `password` - The password of the account.
        
        `**Example**`
        
        ```py
        from pymino import *
        
        bot = Bot()
        bot.run(email=email, password=password)
        response = bot.delete_request_cancel(email=email, password=password)
        print(response)
        ```
        """
        return ApiResponse(await self.session.handler(
            method = "POST",
            url="/g/s/account/delete-request/cancel",
            data={
                "secret": f"0 {password}",
                "deviceID": self.session.generate.device_id(),
                "email": email,
                "timestamp": int(time() * 1000)
            }))

    async def check_device(self, deviceId: str) -> ApiResponse:
        """
        `**check_device**` - Checks if the device is valid.

        `**Parameters**`

        - `deviceId` - The device id of the account.
        
        `**Example**`
        
        ```py
        from pymino import *
        
        bot = Bot()
        response = bot.check_device(deviceId=device_id())
        print(response)
        ```
        """
        return ApiResponse(await self.session.handler(
            method = "POST",
            url="/g/s/device",
            data={
                "deviceID": deviceId,
                "clientType": 100,
                "timezone": -310,
                "systemPushEnabled": True,
                "timestamp": int(time() * 1000)
                }))

    async def fetch_account(self) -> ApiResponse:
        """
        `**fetch_account**` - Fetches the account information.
        
        `**Example**`
        
        ```py
        from pymino import *
        
        bot = Bot()
        bot.run(email=email, password=password)
        response = bot.fetch_account()
        print(response)
        ```
        """
        return ApiResponse(await self.session.handler(method = "GET", url="/g/s/account"))

    async def upload_image(self, image: str) -> str:
        """
        `**upload_image**` - Uploads an image to the server.

        `**Parameters**`

        - `image` - The image to upload.
        
        `**Example**`
        
        ```py
        from pymino import *
        
        bot = Bot()
        bot.run(email=email, password=password)
        response = bot.upload_image(image="image.jpg")
        print(response)
        ```
        """
        return ApiResponse(await self.session.handler(
            method="POST",
            url="/g/s/media/upload",
            data=open(image, "rb").read(),
            content_type="image/jpg"
            )).mediaValue

    async def fetch_profile(self, userId: str) -> UserProfile:
        """
        `**fetch_profile**` - Fetches the profile information.
        
        `**Example**`
        
        ```py
        from pymino import *
        
        bot = Bot()
        bot.run(email=email, password=password)
        response = bot.fetch_profile()
        print(response)
        ```
        """
        return UserProfile(await self.session.handler(
            method = "GET",
            url = f"/g/s/user-profile/{userId}"
            ))

    async def set_amino_id(self, aminoId: str) -> ApiResponse:
        """
        `**set_amino_id**` - Sets the amino id.

        `**Parameters**`

        - `aminoId` - The amino id to set.
        
        `**Example**`
        
        ```py
        from pymino import *
        
        bot = Bot()
        bot.run(email=email, password=password)
        response = bot.set_amino_id(aminoId="aminoId")
        print(response)
        ```
        """
        return ApiResponse(await self.session.handler(
            method="POST",
            url="/g/s/account/change-amino-id",
            data={"aminoId": aminoId, "timestamp": int(time() * 1000)}
            ))

    async def fetch_wallet(self) -> Wallet:
        """
        `**fetch_wallet**` - Fetches the wallet information.
        
        `**Example**`
        
        ```py
        from pymino import *
        
        bot = Bot()
        bot.run(email=email, password=password)
        response = bot.fetch_wallet()
        print(response)
        """
        return Wallet(await self.session.handler(method="GET", url="/g/s/wallet"))

    async def request_security_validation(self, email: str, resetPassword: bool = False) -> ApiResponse:
        """
        `**request_security_validation**` - Requests a security validation.

        `**Parameters**`

        - `email` - The email of the account.

        - `resetPassword` - Whether to reset the password or not.
        
        `**Example**`
        
        ```py
        from pymino import *
        
        bot = Bot()
        response = bot.request_security_validation(email=email)
        print(response)
        ```
        """
        return ApiResponse(await self.session.handler(
            method = "POST",
            url="/g/s/auth/request-security-validation",
            data={
                "identity": email,
                "type": 1,
                "deviceID": self.session.generate.device_id(),
                "level": 2 if resetPassword else None,
                "purpose": "reset-password" if resetPassword else None,
                "timestamp": int(time() * 1000)
            }))

    async def activate_email(self, email: str, code: str) -> ApiResponse:
        """
        `**activate_email**` - Activates an email.

        `**Parameters**`

        - `email` - The email of the account.

        - `code` - The code sent to the email.
        
        `**Example**`
        
        ```py
        from pymino import *
        
        bot = Bot()
        response = bot.activate_email(email=email, code=code)
        print(response)
        ```
        """
        return ApiResponse(await self.session.handler(
            method = "POST",
            url="/g/s/auth/activate-email",
            data={
                "type": 1,
                "identity": email,
                "data": {"code":code},
                "deviceID": self.session.generate.device_id(),
                "timestamp": int(time() * 1000)
            }))

    async def verify(self, email: str, code: str, deviceId: str) -> ApiResponse:
        """
        `**verify**` - Verifies the code sent to the email.

        `**Parameters**`
        
        - `email` - The email of the account.
        
        - `code` - The code sent to the email.

        - `deviceId` - The device id.
        
        `**Example**`
        
        ```py
        from pymino import *
        
        bot = Bot()
        response = bot.verify(email=email, code=code, deviceId=deviceId)
        print(response)
        ```
        """
        return ApiResponse(await self.session.handler(
            method = "POST",
            url="/g/s/auth/check-security-validation",
            data={
                "type": 1,
                "identity": email,
                "data": {"code":code},
                "deviceID": deviceId,
                "timestamp": int(time() * 1000)
            }))

    async def reset_password(self, email: str, newPassword: str, code: str, deviceId: str) -> ResetPassword:
        """
        `**reset_password**` - Resets the password.

        `**Parameters**`

        - `email` - The email of the account.

        - `newPassword` - The new password of the account.

        - `code` - The code sent to the email.
        
        `**Example**`
        
        ```py
        from pymino import *
        
        bot = Bot()
        bot.run(email=email, password=password)
        response = bot.reset_password(email=email, newPassword=newPassword, code=code)
        print(response)
        ```
        """
        return ResetPassword(await self.session.handler(
            method="POST",
            url="/g/s/auth/reset-password",
            data={
                "updateSecret": f"0 {newPassword}",
                "emailValidationContext": {
                    "data": {"code": code},
                    "type": 1,
                    "identity": email,
                    "level": 2,
                    "deviceID": deviceId
                },
                "phoneNumberValidationContext": None,
                "deviceID": deviceId
            }))