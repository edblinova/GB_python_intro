import logging


def input_pos_int(what_quant: str = "", condition: int = 0):
    try:
        n = int(input(f'Введите кол-во {what_quant}: '))
        if n<=condition:
            raise Exception
        return n
    except:
        logging.warning(f'Необходимо ввести целое число больше {condition}!')
        return -1


def input_coin():
    try:
        coin = int(input('Введите решка(1) или герб(0): '))
        if coin!=0 and coin!=1:
            raise Exception
        return coin
    except:
        logging.warning('Необходимо ввести 0 или 1!')
        return -1


def input_int(what_input: str = ""):
    try:
        n = int(input(f'Введите {what_input}: '))
        return n
    except:
        logging.warning('Необходимо ввести целое число!')
        return 0.5


if __name__ == '__main__':
    input_pos_int()
    input_coin()
    input_int()
