# define enumerations using the Enum base class

from enum import Enum, auto

#@unique <- ensures each value can only be used once in the enumeration
class Fruit(Enum):
    APPLE = 1
    BANANA = 2
    ORANGE = 3
    TOMATO = 4
    PEAR = auto()

def main():
    # enums have human-readable values and types
    print(Fruit.APPLE)
    print(type(Fruit.APPLE))
    print(repr(Fruit.APPLE))

    # enums have name and value properties
    print(Fruit.APPLE.value, Fruit.APPLE.name)

    # print the auto-generated value
    print(Fruit.PEAR.value)

    # enums are hashable - can be used as keys
    myFruits = {}
    myFruits[Fruit.BANANA] = "PHONE"
    print(myFruits[Fruit.BANANA])

if __name__ == "__main__":
    main()
