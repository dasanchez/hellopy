def print_fib():
    '''Print out Fibonacci'''
    print('Fibonacci')

def return_fib():
    '''Return Fibonacci'''
    return 'Fibonacci'

print_fib()
print(type(print_fib))
print(type(print_fib()))

return_fib()
print(type(return_fib))
print(type(return_fib()))


def fib(n):
    '''Return the nth number in the Fibonacci sequence'''
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(1))
print(fib(2))
print(fib(8))

help(fib)