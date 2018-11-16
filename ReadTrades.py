import Trade
import datetime

import os.path
from os import path


# TODO: Create and test file reading
# TODO: Create and test Trade creation
# TODO: Create and test price at time function
# TODO: Create and test range function
# TODO: Test max price
# TODO: Test min price
# TODO: Test average price
# TODO: Test standard deviation price
# TODO: Test median price

def read_record(filename):

        try:
            with open(filename) as infile:
                for line in infile:
                    return line
        except FileNotFoundError:
            print("File not found")


def process_trade(record):
    tradeline = record.split("Z")
    time = datetime.datetime.strptime(tradeline[0], "%Y-%m-%dT%H:%M:%S")
    trades = tradeline[1].strip().split(" ")
    trade = Trade.Trade(time, trades[0], trades[1])
    return trade
