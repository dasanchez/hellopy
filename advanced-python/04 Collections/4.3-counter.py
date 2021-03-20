# Demonstrate the usage of Counter objects

from collections import Counter


def main():
    # list of students in class 1
    class1 = ["Bob", "Becky", "Chad", "Darcy", "Frank", "Hannah"
              "Kevin", "James", "James", "Melanie", "Penny", "Steve"]

    # list of students in class 2
    class2 = ["Bill", "Barry", "Cindy", "Debbie", "Frank",
              "Gabby", "Kelly", "James", "Joe", "Sam", "Tara", "Ziggy"]

    # Create a Counter for class1 and class2
    c1 = Counter(class1)
    c2 = Counter(class2)
    
    # How many students in class 1 named James?
    print(f'There are {c1["James"]} students named "James" in class 1.')

    # How many students are in class 1?
    print(f'There are {sum(c1.values())} students in class 1.')

    # Combine the two classes
    c3 = c1.copy()
    c3.update(c2)
    print(f'There are {sum(c3.values())} students between class 1 and 2.')

    # What's the most common name in the two classes?
    print(f'{c3.most_common(1)} is the most common name between class 1 and 2.')

    # Separate the classes again
    c1 = c3.copy()
    c1.subtract(c2)
    print(f'{c1.most_common(1)} is the most common name in class 1.')

    # What's common between the two classes?
    common_names = c1 & c2
    print(common_names)


if __name__ == "__main__":
    main()
