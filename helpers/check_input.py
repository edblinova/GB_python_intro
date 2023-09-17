import logging


def input_pos_int(what_quant: str = "", condition: int = 0):
    while n == -1:
        try:
            n = int(input(f'Введите кол-во {what_quant}: '))
            if n<=condition:
                raise Exception
        except:
            logging.warning(f'Необходимо ввести целое число больше {condition}!')
            n = -1
    return n


def input_coin():
    while coin == -1:
        try:
            coin = int(input('Введите решка(1) или герб(0): '))
            if coin!=0 and coin!=1:
                raise Exception
        except:
            logging.warning('Необходимо ввести 0 или 1!')
            coin = -1
    return coin


def input_int(what_input: str = ""):
    while n == 0.5:
        try:
            n = int(input(f'Введите {what_input}: '))
        except:
            logging.warning('Необходимо ввести целое число!')
            n = 0.5
    return n


if __name__ == '__main__':
    input_pos_int()
    input_coin()
    input_int()
