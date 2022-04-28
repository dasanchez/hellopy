from more.addition import add
from less.subtraction import subtract

def calculate():
    number_1 = 10
    number_2 = 20
    number_3 = 15

    print(f'{number_1} + {number_2} = {add(number_1, number_2)}')
    print(f'{add(number_1, number_2)} - {number_3} = {subtract(add(number_1, number_2),number_3)}')

calculate()
