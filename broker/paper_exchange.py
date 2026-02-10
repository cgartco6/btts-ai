class PaperExchange:
    def __init__(self):
        self.orders = []

    def place_order(self, market, stake, odds):
        self.orders.append({
            "market": market,
            "stake": stake,
            "odds": odds
        })
