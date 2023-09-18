# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума).


import logging
import random

from helpers.check_input import input_int


def main():

    result = []
    my_list = [random.randint(1,1000) for _ in range(100)]

    MINIMUM = input_int('минимум')
    MAXIMUM = input_int('максимум')

    for i in range(len(my_list)):
        if MINIMUM <= my_list[i] <= MAXIMUM:
            result.append(i)
            print(i, end=' ')
    
    logging.warning(f'Результат: {" ".join(result)}')


if __name__ == '__main__':
    main()
