class DrawdownGovernor:
    def __init__(self, max_dd=0.2):
        self.max_dd = max_dd
        self.peak = 0

    def update(self, bankroll):
        self.peak = max(self.peak, bankroll)
        return (self.peak - bankroll) / self.peak < self.max_dd
