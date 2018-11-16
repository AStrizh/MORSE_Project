import statistics
import datetime
import Trade
import ReadTrades

def main():

    filename = "samplefile.txt" #input("Input filename:")

    trades = ReadTrades.read_record(filename)

    for trade in trades:

        print(trade.time)
        print(trade.price)
        print(trade.quantity)
        print("-----------------")

main()
