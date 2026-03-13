import requests

def get_binance_ads():

    url="https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"

    payload={
    "asset":"USDT",
    "fiat":"USD",
    "tradeType":"BUY",
    "page":1,
    "rows":10
    }

    r=requests.post(url,json=payload)

    data=r.json()

    return data["data"]