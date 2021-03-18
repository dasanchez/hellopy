# use iterator functions like enumerate, zip, iter, next


def main():
    # define a list of days in English and French
    days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]

    # use iter to create an iterator over a collection
    # iter1 = iter(days)
    # print(next(iter1))
    # print(next(iter1))
    # print(next(iter1))

    # iterate using a function and a sentinel
    """
    the '' in the iter() call is the sentinel:
    the iterator will stop when the next line read
    contains no characters, ending the loop.
    """
    # with open("testfile.txt", "r") as f:
    #     for line in iter(f.readline, ''):
    #         print(line)

    # use regular iteration over the days
    for day in days:
        print(day)

    # using enumerate reduces code and provides a counter
    for index, day in enumerate(days, start=1):
        print(f"Day {index}: {day}")

    # use zip to combine sequences
    for index, day in enumerate(zip(days, daysFr), start=1):
        print(f"Day {index}: {day[0]} ({day[1]})")

if __name__ == "__main__":
    main()
