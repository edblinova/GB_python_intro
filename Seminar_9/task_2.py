# Узнать какая максимальная households в зоне минимального значения population.


import logging
import pandas as pd


def main():

    try:
        df = pd.read_csv('sample_data/california_housing_train.csv')
        households_max = df[df['population']==df['population'].min()]['households'].max()
        print(households_max)
    
    except Exception as error:
        logging.warning(f'Произошла ошибка при выполнении кода: {error}')


if __name__ == '__main__':
    main()
