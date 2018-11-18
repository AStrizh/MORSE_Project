import Trade
import datetime

"""Functionality for reading Trade data from a provided file name"""


def record_at_time(filename, timevar):
    """ Reads a file of Trades and returns the trade at provided time

        Keyword Arguments:
        filename - Name of the file to read
        timevar - The datetime.datetime to search for
        If there is no trade for that time the file returns adjacent trade data.
    """

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

                    # Addresses the various possibilities of trade times such as:
                    # Trade exists for provided time
                    # The first trade time (and so all others) are past the given date
                    # Given time is between two trades and their average is returned
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

    # If file finishes parsing and all dates are before requested date, returns last trade price on file
    return lasttrade.price


def process_trade(record):
    """ Returns a Trade object from a string of trade data (only accepts UTC 'Z' region code or none)

        Returns None if bad date data

        Keyword Arguments:
        record -  A string in the format 2017-04-25T17:11:55Z 20.18 55
    """

    # Takes out the zulu region code
    tradeline = record.split("Z")

    try:
        time = datetime.datetime.strptime(tradeline[0], "%Y-%m-%dT%H:%M:%S")
    except ValueError:
        print("Cannot format Date/Time from " + record)
        return

    trades = tradeline[1].strip().split(" ")
    trade = Trade.Trade(time, trades[0], trades[1])
    return trade
