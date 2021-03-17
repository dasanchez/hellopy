# Demonstrate the use of variable argument lists

# define a function that takes variable arguments
def addition(*args):
    return sum(args)


def main():
    # pass different arguments
    print(addition(1, 2, 3))
    print(addition(1, 2, 3, 4, 5))

    # pass an existing list
    nums = [10, 25, 50, 100, -175]
    print(addition(*nums))

if __name__ == "__main__":
    main()
