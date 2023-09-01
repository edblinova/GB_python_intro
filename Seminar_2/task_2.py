# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.


import logging


def first_input(question: str = 'сумму'):
    try:
        n = int(input(f'Введите {question} чисел: '))
        if n<=0:
            raise Exception
        return n
    except:
        logging.warning('Необходимо ввести целое число больше 0!')
        return -1


def main():

    while True:

        s = -1
        while s == -1:
            s = first_input()
        
        p = -1
        while p == -1:
            p = first_input('произведение')

        x = 0.5 * (s - (s ** 2 - 4 * p) ** 0.5)
        y = 0.5 * (s + (s ** 2 - 4 * p) ** 0.5)

        try:
            if int(str(x).split('.')[1]) == 0 and int(str(y).split('.')[1]) == 0 and 1<=int(x)<=1000 and 1<=int(y)<=1000:
                print(int(x), int(y))
                break
            else:
                logging.warning('Итоговое решение не является натуральными числами до 1000! Попробуйте загадать снова...')

        except:
            logging.warning('Итоговое решение не является натуральными числами до 1000! Попробуйте загадать снова...')


if __name__ == '__main__':
    main()
