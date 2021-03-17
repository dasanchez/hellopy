# advanced iteration functions in the itertools package
import itertools

def prediFunction(x):
    return x < 10


def main():
    # cycle iterator can be used to cycle over a collection
    seq1 = ["Joe", "John", "Mike"]
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))

    # use count to create a simple counter
    count1 = itertools.count(100, 10)
    print(next(count1))
    print(next(count1))
    print(next(count1))
    
    # accumulate creates an iterator that accumulates values
    vals = [10,20,30,40,50,40,30]
    acc1 = itertools.accumulate(vals, max)
    print(list(acc1))
    acc1 = itertools.accumulate(vals)
    print(next(acc1))
    print(next(acc1))
    print(next(acc1))
 
    # use chain to connect sequences together
    chained = itertools.chain('hello ', 'python')
    print(list(chained))

    # dropwhile and takewhile will return values until
    # a certain condition is met that stops them
    print(list(itertools.dropwhile(prediFunction, [1, 2, 3, 10, 100, 200, 50, 20, 2])))
    print(list(itertools.takewhile(prediFunction, [1, 2, 3, 10, 100, 200, 50, 20, 2])))
    
if __name__ == "__main__":
    main()
    