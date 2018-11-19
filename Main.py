import datetime
import ReadTrades
import ReadStats
from pathlib import Path


def main():
    selection = -1
    while selection is not "0":
        print("---------------------------------------------------")
        print("1 - Get trading price at a date/time.")
        print("2 - Get statistics on trades for a date/time interval.")
        print("0 - Exit")
        selection = input(" Type digit corresponding to your choice: ")

        if selection is "1":
            filename = get_file()
            if filename is not None:
                time = get_time()
                if time is not None:
                    print(ReadTrades.record_at_time(filename, time))
            break
        elif selection is "2":
            filename = get_file()
            if filename is not None:
                print("Enter a start time:")
                time1 = get_time()
                if time1 is not None:
                    print("Enter an end time:")
                    time2 = get_time()
                    if time2 is not None:
                        rs = ReadStats.ReadStats()
                        rs.read_stat_record(filename, time1, time2)

                        print("Max price was: ", rs.get_max())
                        print("Min price was: ", rs.get_min())
                        print("Average price was: ", rs.get_average())
                        print("Standard Deviation: ", rs.get_div())
                        print("Median Price: ", rs.get_median())
            break
        else:
            continue


def get_file():
    filename = -1
    while filename is not "0":
        print("---------------------------------------------------")
        print("Enter a filename to continue or chose one of the other options:")
        print("1 - Go Back")
        print("0 - Exit")
        filename = input("File name: ")
        valid_filename = Path(filename).is_file()

        if filename is "0":
            continue
        if filename is "1":
            main()
            break
        elif valid_filename:
            return filename
        elif not valid_filename:
            print("This file name was invalid!")
            continue

    return None


def get_time():
    selection = -1
    while selection is not "0":
        print("---------------------------------------------------")
        selection = input("Enter datetime in format YYYY-MM-DDTHH:MM:SS : ")
        if selection is 0:
            return None

        try:
            time = datetime.datetime.strptime(selection.strip().replace('Z', ''), "%Y-%m-%dT%H:%M:%S")
            return time

        except ValueError:
            print("Cannot format Date/Time from " + selection)
            continue


main()
