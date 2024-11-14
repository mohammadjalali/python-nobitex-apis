import requests


class GeneralMarketInformation:
    def __init__(self) -> None:
        pass

    def order_books(self):
        return requests.get("https://api.nobitex.ir/v3/orderbook/BTCIRT").json()

    def trade(self):
        return requests.get("https://api.nobitex.ir/v2/trades/BCHIRT").json()

    def market_statistics(self, source_currency: str, destination_currency: str):
        params = {
            "srcCurrency": source_currency,
            "dstCurrency": destination_currency,
        }
        return requests.get("https://api.nobitex.ir/market/stats", params=params).json()

    def ohlc_nobitex_statistics(self, symbol: str, resolution: str, from_, to):
        """
        https://apidocs.nobitex.ir/#ohlc
        """
        params = {
            "symbol": symbol,
            "resolution": resolution,
            "from": from_,
            "to": to,
        }

        return requests.get(
            "https://api.nobitex.ir/market/udf/history", params=params
        ).json()

    def world_market_statistics(self):
        return requests.post("https://api.nobitex.ir/market/global-stats").json()
