# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть


import logging


def first_input():
    try:
        n = int(input('Введите кол-во монеток: '))
        if n<=0:
            raise Exception
        return n
    except:
        logging.warning('Необходимо ввести целое число больше 0!')
        return -1


def second_input():
    try:
        coin = int(input('Введите решка(1) или герб(0): '))
        if coin!=0 and coin!=1:
            raise Exception
        return coin
    except:
        logging.warning('Необходимо ввести 0 или 1!')
        return -1


def main():

    n = -1
    while n == -1:
        n = first_input()

    eagle = 0
    tails = 0

    for _ in range(n):
        
        coin = -1        
        while coin == -1:
            coin = second_input()

        if coin == 0:
            eagle += 1

        else:
            tails += 1
    
    if eagle < tails and eagle!=0:
        logging.warning(f'Необходимо перевернуть {eagle} шт. гербов!')
        print(eagle)

    elif eagle > tails and tails!=0:
        logging.warning(f'Необходимо перевернуть {tails} шт. решек!')
        print(tails)

    elif eagle!=0 or tails!=0:
        logging.warning(f'Ничего переворачивать не нужно!')
        print(0)

    else:
        logging.warning(f'Количество гербов и решек одинаково. Переворачивай, что хочешь!')


if __name__ == '__main__':
    main()
