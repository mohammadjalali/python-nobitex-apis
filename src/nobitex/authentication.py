from typing import Optional, Literal

import requests


class Authentication:
    def __init__(self, key: Optional[str] = None) -> None:
        self._key = key

    def key(self) -> Optional[str]:
        return self._key

    def generate_key(
        self,
        username: str,
        password: str,
        two_factor_authentication_code: Optional[str] = None,
        remember: Literal["yes", "no"] = "no",
    ) -> str:
        """
        https://apidocs.nobitex.ir/#login

        username: Username in nobitex
        password: Password in nobitex
        two_factor_authentication_code: Authentication code if activated
        remember: Generate token for a month or 4 hours. "yes" is for a month and "no" \
            is for 4 hours.  
        """
        headers = {
            "Content-Type": "application/json",
        }
        if two_factor_authentication_code:
            headers["X-TOTP"] = two_factor_authentication_code
        json_data = {
            "username": username,
            "password": password,
            "remember": remember,
            "captcha": "api",
        }
        response = requests.post(
            "https://api.nobitex.ir/auth/login/", headers=headers, json=json_data
        )
        self._key = response.json()["key"]
        return self._key
