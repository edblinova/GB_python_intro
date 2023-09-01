# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N


import logging


def first_input():
    try:
        n = int(input(f'Введите число N: '))
        if n<=0:
            raise Exception
        return n
    except:
        logging.warning('Необходимо ввести целое число больше 0!')
        return -1


def main():

        n = -1
        while n == -1:
            n = first_input()
        
        degree = 0

        while 2 ** degree <= n:

            print(2 ** degree)
            degree += 1


if __name__ == '__main__':
    main()
