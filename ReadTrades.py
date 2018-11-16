import Trade
import datetime


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
                trade = process_trade(line)
                if trade is not None:
                    trades.append(trade)

    except FileNotFoundError:
        print("File not found")
        return

    return trades


def process_trade(record):
    tradeline = record.split("Z")

    try:
        time = datetime.datetime.strptime(tradeline[0], "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        print("Cannot format Date/Time from " + record)
        return

    trades = tradeline[1].strip().split(" ")
    trade = Trade.Trade(time, trades[0], trades[1])
    return trade
