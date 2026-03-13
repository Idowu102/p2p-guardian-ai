blacklisted=set()

def add_scammer(trader_id):

    blacklisted.add(trader_id)

def check_blacklist(trader_id):

    return trader_id in blacklisted