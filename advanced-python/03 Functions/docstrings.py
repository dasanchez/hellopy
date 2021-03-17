# Demonstrate the use of function docstrings


def myFunction(arg1, arg2=None):
    """myFunction(arg1, arg2=None) --> Demonstrates docstrings

    Parameters:
    arg1: the first argument.
    arg2: the second argument. Defaults to None.
    """
    print(arg1, arg2)


def main():
    print(myFunction.__doc__)


if __name__ == "__main__":
    main()
