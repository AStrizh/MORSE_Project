import Trade
import datetime

import os.path
from os import path


# Todo: Catch date format exception
# TODO: Create and test price at time function
# TODO: Create and test range function
# TODO: Test max price
# TODO: Test min price
# TODO: Test average price
# TODO: Test standard deviation price
# TODO: Test median price

def read_record(filename):
    trades = []

    try:
        with open(filename) as infile:
            for line in infile:
                trades.append(process_trade(line))
    except FileNotFoundError:
        print("File not found")
        return

    return trades


def process_trade(record):
    tradeline = record.split("Z")
    time = datetime.datetime.strptime(tradeline[0], "%Y-%m-%dT%H:%M:%S")
    trades = tradeline[1].strip().split(" ")
    trade = Trade.Trade(time, trades[0], trades[1])
    return trade
