import Trade
import datetime
import ReadTrades


class ReadStats:

    def __init__(self):
        self._min = float("inf")
        self._max = 0.0
        self._average = 0.0
        self._total = 0
        self._sum = 0.0
        self._div = 0.0
        self._median = 0.0

    def read_record(self, filename):
        trades = []

        try:
            with open(filename) as infile:
                for line in infile:
                    trade = ReadTrades.process_trade(line)
                    if trade is not None:
                        self.calc_stats(trade)
                        trades.append(trade)

        except FileNotFoundError:
            print("File not found")
            return

        return trades

    def calc_stats(self, trade):
        if float(trade.price) < self._min:
            self._min = float(trade.price)

        if float(trade.price) > self._max:
            self._max = float(trade.price)

    def get_min(self):
        return self._min

    def get_max(self):
        return self._max

    def get_average(self):
        return self._average

    def get_div(self):
        return self._div

    def get_median(self):
        return self._median
