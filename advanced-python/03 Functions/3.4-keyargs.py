# Demonstrate the use of keyword-only arguments


# use keyword-only arguments to help ensure code clarity
def myFunction(*, true_or_false=False):
    print(f"The argument is {true_or_false}")

# use keyword-only arguments to help ensure code clarity
def myFunction2(arg1, *, true_or_false=False):
    print(f"The argument is {true_or_false}")


def main():
    # try to call the function without the keyword
    # myFunction(True) # error: takes 0 positional argumens but 1 was given
    myFunction(true_or_false=True) # also works without arguments
    myFunction2(1, true_or_false=False)

if __name__ == "__main__":
    main()
