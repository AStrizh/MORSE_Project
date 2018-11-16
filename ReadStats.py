import Trade
import datetime
import math
import ReadTrades


class ReadStats:

    def __init__(self):
        self._min = float("inf")
        self._max = 0.0
        self._average = 0.0
        self._totalshares = 0
        self._sumprices = 0.0
        self._div = 0.0
        self._median = 0.0
        self._trades = []

    def read_record(self, filename):

        try:
            with open(filename) as infile:
                for line in infile:
                    trade = ReadTrades.process_trade(line)
                    if trade is not None:
                        self.calc_stats(trade)
                        self.insert_trade(trade)

        except FileNotFoundError:
            print("File not found")
            return

        return self._trades

    def insert_trade(self, newtrade):

        i = 0
        for trade in self._trades:
            if float(newtrade.price) > float(trade.price):
                i += 1
            else:
                break

        self._trades.insert(i, newtrade)

    def calc_stats(self, trade):
        if float(trade.price) < self._min:
            self._min = float(trade.price)

        if float(trade.price) > self._max:
            self._max = float(trade.price)

        self._totalshares += int(trade.quantity)
        self._sumprices += (float(trade.price) * int(trade.quantity))

    def get_min(self):
        return self._min

    def get_max(self):
        return self._max

    def get_average(self):
        return round(self._sumprices / self._totalshares, 2)

    def get_div(self):
        average = round(self._sumprices / self._totalshares, 2)
        divsum = 0.0
        for trade in self._trades:
            divsum += int(trade.quantity) * ((float(trade.price) - average) ** 2)

        variance = divsum / self._totalshares
        return math.sqrt(variance)

    def get_median(self):

        if self._totalshares % 2 == 0:
            middle = self._totalshares / 2

            total = 0
            i = 0
            for trade in self._trades:
                total += int(trade.quantity)
                if total > middle + 1:
                    return trade.price

                elif total == middle or total == middle + 1:

                    return round((float(self._trades[i].price) +
                                  float(self._trades[i + 1].price)) / 2, 2)

                else:
                    i += 1

            return 0

        else:
            middle = self._totalshares / 2 + 1
            total = 0
            for trade in self._trades:
                total += int(trade.quantity)
                if total >= middle:
                    return trade.price

            return 0
