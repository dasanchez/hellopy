from functools import wraps

def bold(func):
    '''Bold decorator'''
    @wraps(func)
    def wrapper():
        '''return html bold tags'''
        result = '<b>' + func() + '</b>'
        return result
    return wrapper

def italic(func):
    '''Italic decorator'''
    @wraps(func)
    def wrapper():
        '''return html italic tags'''
        result = '<i>' + func() + '</i>'
        return result
    return wrapper

@bold
@italic
def printfib():
    '''return Fibonacci'''
    return 'Fibonacci'

print(printfib())
print(printfib.__name__)
print(printfib.__doc__)