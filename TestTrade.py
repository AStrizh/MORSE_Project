import unittest
import Trade
import datetime


class TestTrade(unittest.TestCase):

    def test_Trade_initialization(self):
        time = datetime.datetime.strptime("2017-04-25T17:11:55", "%Y-%m-%dT%H:%M:%S")
        price = 27.36
        quantity = 73

        trade = Trade.Trade(time, price, quantity)

        self.assertEqual(trade.time, datetime.datetime.strptime("2017-04-25T17:11:55", "%Y-%m-%dT%H:%M:%S"),
                         "The date does not match")
        self.assertEqual(trade.price, price, "The price does not match")
        self.assertEqual(trade.quantity, quantity, "The quantity does not match")
