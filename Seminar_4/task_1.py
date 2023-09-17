# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.


# Пользователь вводит 2 числа. 
# n — кол-во элементов первого множества. 
# m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.


import logging
from helpers.check_input import input_pos_int, input_int


def main():

    n_set = set()
    m_set = set()

    n = input_pos_int('элементов первого множества')
    m = input_pos_int('элементов второго множества')

    for _ in range(n):
        
        new_el = input_int('элемент первого множества')
        n_set.add(new_el)
    
    for _ in range(m):
        
        new_el = input_int('элемент второго множества')
        m_set.add(new_el)
    
    result = sorted(n_set.intersection(m_set))
    logging.warning(f'Результат: {result}')


if __name__ == '__main__':
    main()
