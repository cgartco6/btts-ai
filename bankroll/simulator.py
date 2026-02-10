class BankrollSimulator:
    def __init__(self, bankroll=1000):
        self.bankroll = bankroll

    def stake(self, ev, confidence):
        return self.bankroll * min(0.02, ev * confidence)

    def settle(self, win, stake, odds):
        if win:
            self.bankroll += stake * (odds - 1)
        else:
            self.bankroll -= stake
