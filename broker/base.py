from abc import ABC, abstractmethod

class Broker(ABC):
    @abstractmethod
    def get_markets(self): pass

    @abstractmethod
    def place_order(self, market_id, side, stake, price): pass

    @abstractmethod
    def settle(self, order_id, outcome): pass
