import statistics
import datetime
import Trade


def main():

    # time = datetime.datetime.strptime("2017-04-25T17:11:55", "%Y-%m-%dT%H:%M:%S")
    # print(time)
    # trade = Trade.Trade(time, 15, 27)
    #
    # print(trade.time)
    # print(trade.price)
    # print(trade.quantity)

    filename = "samplefile.txt" #input("Input filename:")
    with open(filename) as infile:
        for line in infile:

            tradeline = line.split("Z")
            time = datetime.datetime.strptime(tradeline[0], "%Y-%m-%dT%H:%M:%S")
            trades = tradeline[1].strip().split(" ")
            trade = Trade.Trade(time, trades[0], trades[1])

            print(trade.time)
            print(trade.price)
            print(trade.quantity)
            print("-----------------")

    # print(time)
    # print(time + datetime.timedelta(days=3, hours=5, weeks=2))
    # print()
    # print(datetime.datetime.now())

    # data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
    # print("The mean is ", statistics.mean(data))
    # print("The standard deviation is ", statistics.stdev(data))
    # print("The median is ", statistics.median(data))
    # print("The max is ", str(max(data)))


main()
