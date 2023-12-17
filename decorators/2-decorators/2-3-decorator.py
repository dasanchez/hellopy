def uppercase(a):
    '''Decorator function'''
    def wrapper():
        '''Returns uppercased result'''
        return a().upper() 
    return wrapper

@uppercase
def pfib():
    '''Return Fibonacci'''
    return 'Fibonacci'

print(pfib)
print(pfib())