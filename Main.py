import statistics
import datetime
import Trade
import ReadTrades
import ReadStats


def main():
    fileinput = input("Input filename: ")

    timeinput = input("Input a time: ")
    print(ReadTrades.record_at_time(fileinput, timeinput))

    timeinput1 = input("Input a start time: ")
    timeinput2 = input("Input an end time: ")

    try:
        time1 = datetime.datetime.strptime(timeinput1.strip().replace('Z', ''), "%Y-%m-%dT%H:%M:%S")

    except ValueError:
        print("Cannot format Start time")
        return

    try:
        time2 = datetime.datetime.strptime(timeinput2.strip().replace('Z', ''), "%Y-%m-%dT%H:%M:%S")

    except ValueError:
        print("Cannot format End time")
        return

    rs = ReadStats.ReadStats()
    rs.read_stat_record(fileinput, time1, time2)

    print("Max price was: " + str(rs.get_max()))
    print("Min price was: " + str(rs.get_min()))
    print("Average price was: " + str(rs.get_average()))
    print("Standard Deviation: " + str(rs.get_div()))
    print("Median Price: " + str(rs.get_median()))


main()
