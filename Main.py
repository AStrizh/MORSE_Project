import statistics
import datetime
import Trade
import ReadTrades


def main():
    filename = "samplefile.txt"  # input("Input filename:")

    # trades = ReadTrades.read_record(filename)
    #
    # for trade in trades:
    #     print(trade.time)
    #     print(trade.price)
    #     print(trade.quantity)
    #     print("-----------------")

    price = ReadTrades.record_at_time(filename, "2017-05-19T05:49:34Z")
    print(price)


main()
