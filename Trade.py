class Trade:

    def __init__(self, time, price, quantity):
        self._time = time
        self._price = price
        self._quantity = quantity

    @property
    def time(self):
        return self._time

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity
