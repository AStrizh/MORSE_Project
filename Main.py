def main():
    filename = input("Input filename:")
    with open(filename) as infile:
        for line in infile:
            print(line, end='')


main()
