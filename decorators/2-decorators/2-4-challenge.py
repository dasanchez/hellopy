def make_posh(func):
    def wrapper():
        result = func()
        pre_content = '+' + '-'*(len(result)-2) + '+\n' + \
                      '|' + ' '*(len(result)-2) + '|\n'
        post_content= '\n|' + ' '*(len(result)-2) + '|\n' + \
                      '+' + '='*(len(result)-2) + '+\n'
        print(pre_content+result+post_content)
        return result
    return wrapper
 
@make_posh
def pfib():
    '''Return Fibonacci'''
    return ' Fibonacci '

pfib()