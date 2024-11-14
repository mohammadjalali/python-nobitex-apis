from typing import Any, Mapping

import requests

import nobitex.config as config


class User:
    def __init__(self) -> None:
        pass

    def balance(self, currency: str) -> Mapping[Any, Any]:
        headers = {
            "Authorization": f"Token {config.KEY}",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        data = f'{"currency":"{currency}"}'
        return requests.post(
            "https://api.nobitex.ir/users/wallets/balance", headers=headers, data=data
        ).json()

    def transactions(self) -> Mapping[Any, Any]:
        headers = {
            "Authorization": "Token yourTOKENhereHEX0000000000",
        }
        params = {
            "wallet": "4159",
        }

        return requests.get(
            "https://api.nobitex.ir/users/wallets/transactions/list",
            params=params,
            headers=headers,
        ).json()
