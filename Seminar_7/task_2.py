# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).


import logging


def main():

    def print_operation_table(operation, num_rows=6, num_columns=6):
        result = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
        for row in result:
            print(*[f"{item:>2}" for item in row])
    
    try:
        print_operation_table(lambda x, y: x * y)
    
    except Exception as error:
        logging.warning(f'Произошла ошибка при выполнении кода: {error}')


if __name__ == '__main__':
    main()
