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

        cls.fakestart = datetime.datetime.strptime("2005-07-02T12:03:22", "%Y-%m-%dT%H:%M:%S")
        cls.fakeend = datetime.datetime.strptime("2030-07-02T12:03:22", "%Y-%m-%dT%H:%M:%S")

        cls.fakefile = "2017-03-01T13:37:89Z 21.37 100\n" + \
                       "2017-04-25T17:11:55Z 20.18 55\n" + \
                       "2017-05-19T05:49:34Z 23.09 21\n" + \
                       "2017-06-12T09:51:21Z 17.21 80000"

        cls.otherfakefile = "2010-03-01T13:37:12Z 11 19\n" + \
                            "2011-04-25T17:11:55Z 12 47\n" + \
                            "2011-13-25T17:11:55Z 23 89\n" + \
                            "2012-05-19T05:49:34Z 13 56\n" + \
                            "2013-05-19T05:49:34Z 14 65\n" + \
                            "2013-05-19T05:49:63Z 14 65\n" + \
                            "2014-05-19T05:49:34Z 15 47\n" + \
                            "2015-05-19T05:49:34Z 16 36\n" + \
                            "2016-05-19T05:49:34Z 17 20\n" + \
                            "2017-05-19T05:49:34Z 18 10\n" + \
                            "2019-05-19T05:49:34Z 19 10\n" + \
                            "2019-06-12T09:51:21Z 20 6"

    def test_CanThrowReadException(self):
        self.assertRaises(FileNotFoundError, ReadStats.ReadStats().read_stat_record("fakefile.txt",
                                                                                    self.fakestart, self.fakeend))

    def test_CanReadFile(self):
        with patch("builtins.open", mock_open(read_data="2017-04-25T17:11:55Z 20.18 55")):
            trades = ReadStats.ReadStats().read_stat_record("path/to/open", self.fakestart, self.fakeend)
            self.assertEqual(float(trades[0].price), 20.18, "The price does not match")

    def test_CalcMin(self):
        with patch("builtins.open", mock_open(read_data=self.fakefile)):
            rs = ReadStats.ReadStats()
            rs.read_stat_record(self.fakefile, self.fakestart, self.fakeend)
            self.assertEqual(rs.get_min(), 17.21)

    def test_CalcMax(self):
        with patch("builtins.open", mock_open(read_data=self.fakefile)):
            rs = ReadStats.ReadStats()
            rs.read_stat_record(self.fakefile, self.fakestart, self.fakeend)
            self.assertEqual(rs.get_max(), 23.09)

    def test_CalcAverage(self):
        with patch("builtins.open", mock_open(read_data=self.fakefile)):
            rs = ReadStats.ReadStats()
            rs.read_stat_record(self.fakefile, self.fakestart, self.fakeend)
            self.assertEqual(rs.get_average(), 17.21)

    def test_CalcDiv(self):
        with patch("builtins.open", mock_open(read_data=self.otherfakefile)):
            rs = ReadStats.ReadStats()
            rs.read_stat_record(self.fakefile, self.fakestart, self.fakeend)
            self.assertTrue(2.091 > rs.get_div() > 2.0909)

    # def test_TradesInOrder(self):
    #     with patch("builtins.open", mock_open(read_data=self.fakefile)):
    #         rs = ReadStats.ReadStats()
    #         for trade in rs.read_stat_record(self.fakefile, self.fakestart, self.fakeend):
    #             print(trade.price, end=" ")

    def test_CalcMedianEven(self):
        with patch("builtins.open", mock_open(read_data=self.fakefile)):
            rs = ReadStats.ReadStats()
            rs.read_stat_record(self.fakefile, self.fakestart, self.fakeend)
            self.assertEqual(float(rs.get_median()), 17.21)

    def test_CalcMedianOdd(self):
        fakeeven = "2017-04-25T17:11:55Z 20.18 55\n" + \
                   "2017-05-19T05:49:34Z 23.09 20\n"

        with patch("builtins.open", mock_open(read_data=fakeeven)):
            rs = ReadStats.ReadStats()
            rs.read_stat_record(self.fakefile, self.fakestart, self.fakeend)
            self.assertEqual(float(rs.get_median()), 20.18)

    def test_CalcMedianSmaller(self):
        fakeeventhis = "2017-03-01T13:37:29Z 19.37 4\n" + \
                       "2017-04-25T17:11:55Z 20.18 4\n" + \
                       "2017-05-19T05:49:34Z 23.09 3\n" + \
                       "2017-06-12T09:51:21Z 25.21 3"

        with patch("builtins.open", mock_open(read_data=fakeeventhis)):
            rs = ReadStats.ReadStats()
            rs.read_stat_record(self.fakefile, self.fakestart, self.fakeend)
            self.assertEqual(float(rs.get_median()), 21.63)

    def test_CalcDateRange(self):
        teststart = datetime.datetime.strptime("2012-04-02T12:03:22", "%Y-%m-%dT%H:%M:%S")
        testend = datetime.datetime.strptime("2017-06-02T12:03:22", "%Y-%m-%dT%H:%M:%S")

        with patch("builtins.open", mock_open(read_data=self.otherfakefile)):
            rs = ReadStats.ReadStats()
            rs.read_stat_record(self.fakefile, teststart, testend)

            self.assertTrue(1.43 > rs.get_div() > 1.42)
            self.assertEqual(float(rs.get_average()), 14.7)

