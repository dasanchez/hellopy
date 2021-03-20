# use transform functions like sorted, filter, map


def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False


def isVowel(x):
    vowels = 'aAeEiIoOuU'
    if x in vowels:
        return True
    else:
        return False

def squareFunc(x):
    return x*x

def toGrade(x):
    if x >= 90:
        return 'A'
    elif x >= 80:
        return 'B'
    elif x >= 70:
        return 'C'
    elif x >= 60:
        return 'D'
    else:
        return 'F'

def main():
    # define some sample sequences to operate on
    nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
    chars = "abcDeFGHiJklmnoP"
    grades = (81, 89, 94, 78, 61, 66, 99, 74)

    # use filter to remove items from a list
    evens = list(filter(isEven, nums))
    print(evens)

    # use filter on non-numeric sequence
    vow = list(filter(isVowel, chars))
    print(vow)

    # use map to create a new sequence of values
    squares = list(map(squareFunc, nums))
    print(squares)

    # use sorted and map to change numbers to grades
    gradeLetters = list(map(toGrade, sorted(grades, reverse=True)))
    print(gradeLetters)

if __name__ == "__main__":
    main()
