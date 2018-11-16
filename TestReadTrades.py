import unittest
from unittest.mock import patch, mock_open
import Trade
import datetime
import ReadTrades


class TestStringMethods(unittest.TestCase):

    def test_CanThrowReadException(self):
        self.assertRaises(FileNotFoundError, ReadTrades.read_record("fakefile.txt"))

    def test_CanReadFile(self):
        with patch("builtins.open", mock_open(read_data="2017-04-25T17:11:55Z 20.18 55")):
            trades = ReadTrades.read_record("path/to/open")
            self.assertEqual(float(trades[0].price), 20.18, "The price does not match")

    def test_CanCreateTrade(self):
        trade = ReadTrades.process_trade("2017-04-25T17:11:55Z 20.18 55")
        self.assertEqual(trade.time, datetime.datetime.strptime("2017-04-25T17:11:55", "%Y-%m-%dT%H:%M:%S"),
                         "The date does not match")
        self.assertEqual(float(trade.price), 20.18, "The price does not match")
        self.assertEqual(int(trade.quantity), 55, "The quantity does not match")
