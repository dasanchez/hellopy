# Demonstrate the usage of OrderedDict objects

from collections import OrderedDict


def main():
    # list of sport teams with wins and losses
    sportTeams = [("Royals", (18, 12)), ("Rockets", (24, 6)), 
                ("Cardinals", (20, 10)), ("Dragons", (22, 8)),
                ("Kings", (15, 15)), ("Chargers", (20, 10)), 
                ("Jets", (16, 14)), ("Warriors", (25, 5))]

    # sort the teams by number of wins
    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)

    # create an ordered dictionary of the teams
    od = OrderedDict(sortedTeams)
    print(od)

    # Use popitem to remove the top item
    removed_item = od.popitem(last=False)
    print(f'With the {removed_item[0]} team gone ({removed_item[1]}), the ordered dict is now:\n{od}')
    
    # What are next the top 4 teams?
    for index, team in enumerate(od, start=1):
        print(f'{index}: {team}')
        if index == 4:
            break

    # test for equality
    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "c": 3, "b": 2})
    print("Equality test: ", a == b)

if __name__ == "__main__":
    main()
