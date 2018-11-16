import unittest
from unittest.mock import patch, mock_open
import Trade
import datetime
import ReadTrades
import ReadStats


class TestReadStats(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        time = datetime.datetime.strptime("2012-07-02T12:03:22", "%Y-%m-%dT%H:%M:%S")
        cls.faketrade = Trade.Trade(time, 13.97, 137)

        cls.fakefile = "2017-03-01T13:37:89Z 21.37 100\n" + \
                       "2017-04-25T17:11:55Z 20.18 55\n" + \
                       "2017-05-19T05:49:34Z 23.09 21\n" + \
                       "2017-06-12T09:51:21Z 17.21 80000"

    def test_CanThrowReadException(self):
        self.assertRaises(FileNotFoundError, ReadStats.ReadStats().read_record("fakefile.txt"))

    def test_CanReadFile(self):
        with patch("builtins.open", mock_open(read_data="2017-04-25T17:11:55Z 20.18 55")):
            trades = ReadStats.ReadStats().read_record("path/to/open")
            self.assertEqual(float(trades[0].price), 20.18, "The price does not match")

    def testCalcMin(self):
        with patch("builtins.open", mock_open(read_data=self.fakefile)):
            rs = ReadStats.ReadStats()
            rs.read_record(self.fakefile)
            self.assertEqual(rs.get_min(), 17.21)

    def testCalcMax(self):
        with patch("builtins.open", mock_open(read_data=self.fakefile)):
            rs = ReadStats.ReadStats()
            rs.read_record(self.fakefile)
            self.assertEqual(rs.get_max(), 23.09)

    def testCalcAverage(self):
        with patch("builtins.open", mock_open(read_data=self.fakefile)):
            rs = ReadStats.ReadStats()
            rs.read_record(self.fakefile)
            self.assertEqual(rs.get_average(), 17.21)
