import Trade
import datetime


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


def record_at_time(filename, timevar):
    timevar = timevar.strip().replace('Z', '')
    lasttrade = None

    try:
        time = datetime.datetime.strptime(timevar, "%Y-%m-%dT%H:%M:%S")

    except ValueError:
        print("Cannot format Date/Time from " + timevar)
        return

    try:
        with open(filename) as infile:

            for line in infile:
                trade = process_trade(line)
                if trade is not None:

                    if trade.time == time:
                        return trade.price
                    elif trade.time < time:
                        lasttrade = trade
                    else:
                        if lasttrade is None:
                            return trade.price

                        tempprice = (float(trade.price) * float(trade.quantity)
                                     + float(lasttrade.price) * float(lasttrade.quantity)) \
                                    / (float(trade.quantity) + float(lasttrade.quantity))

                        return round(tempprice, 2)

    except FileNotFoundError:
        print("File not found")
        return

    return lasttrade.price


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
