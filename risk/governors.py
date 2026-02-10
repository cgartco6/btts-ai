class RiskGovernor:
    def __init__(self, max_stake_pct=0.02):
        self.max_stake_pct = max_stake_pct

    def approve(self, bankroll, stake):
        return stake <= bankroll * self.max_stake_pct
