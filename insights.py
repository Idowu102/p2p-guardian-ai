def generate_trade_insight(
        market_price,
        trader_price,
        trust_score):

    diff = trader_price - market_price

    if diff > 5:
        advice = "Price is higher than market."

    elif diff < -5:
        advice = "Price is lower than market."

    else:
        advice = "Price is close to market."

    if trust_score < 60:
        advice += " Trader has low trust."

    elif trust_score > 85:
        advice += " Trader is highly trusted."

    return {
        "market_price": market_price,
        "trader_price": trader_price,
        "difference": diff,
        "trust_score": trust_score,
        "advice": advice
    }