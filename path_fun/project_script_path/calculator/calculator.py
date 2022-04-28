def calculate():
    number_1 = 10
    number_2 = 20
    number_3 = 15

    print(f'{number_1} + {number_2} = {add(number_1, number_2)}')
    print(f'{add(number_1, number_2)} - {number_3} = {subtract(add(number_1, number_2),number_3)}')


if __name__ == '__main__':
    import os
    import sys
    
    PROJECT_ROOT = os.path.abspath(os.path.join(
                      os.path.dirname(__file__), 
                      os.pardir)
    )
    sys.path.append(PROJECT_ROOT)

    from more.addition import add
    from less.subtraction import subtract

    calculate()