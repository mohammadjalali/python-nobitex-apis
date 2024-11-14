from typing import Optional, Mapping, Literal, Any

import requests
import nobitex.config as config

ExecutionType = Literal["stop_limit", "market", "limit", "stop_limit"]
TradeType = Literal["spot", "margin"]


class MarketSpot:
    def __init__(self) -> None:
        pass

    def add_order(
        self,
        order_type: str,
        source_currency: str,
        destination_currency: str,
        amount: str,
        price: str,
        order_id: Optional[str],
    ) -> Mapping[Any, Any]:
        headers = {
            "Authorization": f"Token {config.KEY}",
            "content-type": "application/json",
        }

        json_data = {
            "type": order_type,
            "srcCurrency": source_currency,
            "dstCurrency": destination_currency,
            "amount": amount,
            "price": price,
            "clientOrderId": order_id,
        }

        return requests.post(
            "https://api.nobitex.ir/market/orders/add", headers=headers, json=json_data
        ).json()

    def orders_status(
        self, order_id: Optional[int], client_order_id: Optional[str]
    ) -> Mapping[Any, Any]:
        headers = {
            "Authorization": f"Token {config.KEY}",
            "content-type": "application/json",
        }
        json_data = {}

        if order_id:
            json_data["id"] = order_id
        if client_order_id:
            json_data["clientOrderId"] = client_order_id

        return requests.post(
            "https://api.nobitex.ir/market/orders/status",
            headers=headers,
            json=json_data,
        ).json()

    def orders(
        self,
        status: Literal["all", "open", "done", "close"],
        order_type: Literal["sell", "buy"],
        execution: ExecutionType,
        trade_type: TradeType,
        source_currency: str,
        destination_currency: str,
        details: int,
        form_id: int,
        order: str,
    ) -> Mapping[Any, Any]:

        headers = {
            "Authorization": f"Token {config.KEY}",
        }

        params = {
            "status": status,
            "type": order_type,
            "execution": execution,
            "tradeType": trade_type,
            "srcCurrency": source_currency,
            "dstCurrency": destination_currency,
            "details": details,
            "form_id": form_id,
            "order": order,
        }

        return requests.get(
            "https://api.nobitex.ir/market/orders/list", params=params, headers=headers
        ).json()

    def update_order_status(
        self, order_id: int, client_order_id: Optional[str], status: Optional[str]
    ):
        headers = {
            "Authorization": f"Token {config.KEY}",
            "content-type": "application/json",
        }
        json_data = {
            "status": status,
        }

        if order_id:
            json_data["order"] = order_id
        if client_order_id:
            json_data["clientOrderId"] = client_order_id

        return requests.post(
            "https://api.nobitex.ir/market/orders/update-status",
            headers=headers,
            json=json_data,
        ).json()

    def cancel_orders(
        self,
        hours: Optional[float],
        execution: Optional[ExecutionType],
        trade_type: Optional[TradeType],
        source_currency: Optional[str],
        destination_currency: Optional[str],
    ) -> Mapping[Any, Any]:
        headers = {
            "Authorization": f"Token {config.KEY}",
            "content-type": "application/json",
        }
        json_data = self._add_full_variables(
            hours=hours,
            execution=execution,
            tradeType=trade_type,
            srcCurrency=source_currency,
            dstCurrency=destination_currency,
        )

        return requests.post(
            "https://api.nobitex.ir/market/orders/cancel-old",
            headers=headers,
            json=json_data,
        ).json()

    def trades(
        self,
        source_currency: Optional[str],
        destination_currency: Optional[str],
        from_id: Optional[int],
    ) -> Mapping[Any, Any]:
        headers = {
            "Authorization": f"Token {config.KEY}",
        }

        params = self._add_full_variables(
            source_currency, destination_currency, from_id
        )

        return requests.get(
            "https://api.nobitex.ir/market/trades/list", params=params, headers=headers
        ).json()

    def _add_full_variables(**kwargs: Mapping[Any, Any]):
        json_data = {}
        for key, value in kwargs.items():
            if value:
                json_data[key] = value
        return json_data
