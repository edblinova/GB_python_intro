# Работать с файлом california_housing_train.csv, который находится в папке sample_data. 
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).


import logging
import pandas as pd


def main():

    try:
        df = pd.read_csv('sample_data/california_housing_train.csv')
        median_house_value_mean = df[(0<=df['population']) & (df['population']<=500)]['median_house_value'].mean()
        print(median_house_value_mean)
    
    except Exception as error:
        logging.warning(f'Произошла ошибка при выполнении кода: {error}')


if __name__ == '__main__':
    main()
