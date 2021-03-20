# Demonstrate how to use set comprehensions


def main():
    # define a list of temperature data points
    ctemps = [5, 10, 12, 14, 10, 23, 41, 30, 12, 24, 12, 18, 29]

    # build a set of unique Fahrenheit temperatures
    ftemps1 = [(t * 9/5) + 32 for t in ctemps]
    ftemps2 = {(t * 9/5) + 32 for t in ctemps}
    print(sorted(ftemps1))
    print(ftemps2)

    # build a set from an input source
    sTemp = "The quick brown fox jumped over the lazy dog"
    charsList = [c.upper() for c in sTemp if not c.isspace()]
    charsSet = {c.upper() for c in sTemp if not c.isspace()}
    print(f"{len(charsList)} elements in charsList: {charsList}")
    print(f"{len(charsSet)} elements in charsSet: {charsSet}")


if __name__ == "__main__":
    main()
