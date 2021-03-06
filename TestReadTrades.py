import unittest
from unittest.mock import patch, mock_open
import datetime
import ReadTrades


class TestReadTrades(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.fakefile = "2017-03-01T13:37:89Z 21.37 100\n" + \
                       "2017-04-25T17:11:55Z 20.18 55\n" + \
                       "2017-05-19T05:49:34Z 23.09 21\n" + \
                       "2017-06-12T09:51:21Z 17.21 80000"

    def test_CanCatchBadDate(self):
        self.assertRaises(ValueError, ReadTrades.process_trade("2017-03-01T13:37:89Z 21.37 100"))

    def test_CanCreateTrade(self):
        trade = ReadTrades.process_trade("2017-04-25T17:11:55Z 20.18 55")
        self.assertEqual(trade.time, datetime.datetime.strptime("2017-04-25T17:11:55", "%Y-%m-%dT%H:%M:%S"),
                         "The date does not match")
        self.assertEqual(trade.price, 20.18, "The price does not match")
        self.assertEqual(trade.quantity, 55, "The quantity does not match")

    def test_RecordAtTimeThrowReadException(self):
        self.assertRaises(FileNotFoundError, ReadTrades.record_at_time("fakefile.txt", "2017-04-25T17:11:55Z 20.18 55"))

    def test_CanReturnRecordAtTime(self):
        with patch("builtins.open", mock_open(read_data="2017-05-19T05:49:34Z 23.09 21")):
            time = datetime.datetime.strptime("2017-05-19T05:49:34", "%Y-%m-%dT%H:%M:%S")
            price = ReadTrades.record_at_time("path/to/open", time)
            self.assertTrue(float(price) == 23.09)

    def test_CanAverageRecordAtTime(self):
        with patch("builtins.open", mock_open(read_data=self.fakefile)):
            time = datetime.datetime.strptime("2017-04-29T17:11:55", "%Y-%m-%dT%H:%M:%S")
            price = ReadTrades.record_at_time("path/to/open", time)
            self.assertTrue(float(price) == 20.98)

    def test_RecordAtTimeEarly(self):
        with patch("builtins.open", mock_open(read_data=self.fakefile)):
            time = datetime.datetime.strptime("2016-04-29T17:11:55", "%Y-%m-%dT%H:%M:%S")
            price = ReadTrades.record_at_time("path/to/open", time)
            self.assertTrue(float(price) == 20.18)

    def test_RecordAtTimeLate(self):
        with patch("builtins.open", mock_open(read_data=self.fakefile)):
            time = datetime.datetime.strptime("2018-04-29T17:11:55", "%Y-%m-%dT%H:%M:%S")
            price = ReadTrades.record_at_time("path/to/open", time)
            self.assertTrue(float(price) == 17.21)
