import time
from scraper import get_binance_ads
from fraud_model import predict_scammer
from trust_score import calculate_trust_score
from database import save_trader
from blacklist import add_scammer

def monitor_binance():

    print("Monitoring Binance P2P traders...")

    while True:

        ads=get_binance_ads()

        for ad in ads:

            trader=ad["advertiser"]

            trader_id=trader["nickName"]

            completion=float(trader["monthFinishRate"])*100

            orders=trader["monthOrderCount"]

            cancel_rate=max(0,100-completion)

            account_age=365
            disputes=0
            volume=orders

            trust=calculate_trust_score(
            completion,
            cancel_rate,
            account_age,
            disputes,
            volume
            )

            risk=predict_scammer(
            completion,
            cancel_rate,
            account_age,
            disputes
            )

            save_trader(trader_id,trust,risk)

            if risk=="High Risk":

                add_scammer(trader_id)

                print("⚠ High Risk Binance Trader:",trader_id)

        time.sleep(60)