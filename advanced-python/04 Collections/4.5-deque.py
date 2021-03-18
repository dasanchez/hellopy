# deque objects are like double-ended queues

import collections
import string

def print_letters(deq):
    for letter in deq:
        print(letter.upper(), end=" ")
    print()

def main():
    
    # initialize a deque with lowercase letters
    d = collections.deque(string.ascii_lowercase)
    print(d)

    # deques support the len() function
    print(len(d))

    # deques can be iterated over
    print_letters(d)

    # manipulate items from either end
    d.pop()
    print_letters(d)
    d.popleft()
    print_letters(d)
    d.append('9')
    print_letters(d)
    d.appendleft('1')
    print_letters(d)

    # rotate the deque
    d.rotate(3)
    print_letters(d)
    d.rotate(-2)
    print_letters(d)

if __name__ == "__main__":
    main()
