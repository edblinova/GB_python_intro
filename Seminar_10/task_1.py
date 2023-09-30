# В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. 
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()


import logging

import pandas as pd
import random


def main():

    try:
        lst = ['robot'] * 10
        lst += ['human'] * 10
        random.shuffle(lst)
        data = pd.DataFrame({'whoAmI':lst})
        data['whoAmI'] = data['whoAmI'].apply(lambda x: 1 if x=='human' else 0)
        print(data.head())
    
    except Exception as error:
        logging.warning(f'Произошла ошибка при выполнении кода: {error}')


if __name__ == '__main__':
    main()
