# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: a<sub>n</sub> = a<sub>1</sub> + (n-1) * d.
# Каждое число вводится с новой строки.


import logging
from helpers.check_input import input_int


def main():

    result = []

    first_element = input_int('первый элемент арифметической прогрессии')
    difference = input_int('разность')
    n = input_int('количество элементов')

    result.append(first_element)

    for i in range(1, n+1, 1):

        element = first_element + (i-1) * difference
        result.append(element)

        print(element, end=' ')
    
    logging.warning(f'Арифметическая прогрессия: {" ".join(result)}')


if __name__ == '__main__':
    main()
