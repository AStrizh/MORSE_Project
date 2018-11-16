import unittest
from unittest.mock import patch, mock_open
import Trade
import datetime
import ReadTrades


class TestStringMethods(unittest.TestCase):

    def test_CanThrowReadException(self):
        self.assertRaises(FileNotFoundError, ReadTrades.read_record("fakefile.txt"))

    def test_CanReadFile(self):
        with patch("builtins.open", mock_open(read_data="data")) as mock_file:
            assert ReadTrades.read_record("path/to/open") == "data"

