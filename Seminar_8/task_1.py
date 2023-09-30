# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных.


import logging

from open_file import open_file
from save_file import save_file
from show_contacts import show_contacts
from save_contact import save_contact
from find_contact import find_contact
from change_contact import change_contact
from delete_contact import delete_contact


def main():

    menu = '''Главное меню
            1. Открыть файл
            2. Сохранить файл
            3. Показать все контакты
            4. Создать контакт
            5. Найти контакт
            6. Изменить контакт
            7. Удалить контакт
            8. Выход'''

    try:
        phone_book = {}
        
        while True:
            print(menu)

            choice = input('Выберите пункт меню: ')
            
            match choice:
                case '1':
                    phone_book = open_file()
                    print('\nТелефонная книга успешно загружена!\n')
                case '2':
                    save_file(phone_book)
                    print('\nТелефонная книга успешно сохранена!\n')
                case '3':
                    print('\nТелефонная книга:\n')
                    show_contacts(phone_book)
                case '4': 
                    contact = save_contact(phone_book)
                    print(f'\nКонтакт {contact} успешно сохранён!\n')
                case '5':
                    contact = find_contact(phone_book)
                    show_contacts(contact)
                case '6':
                    contact = change_contact(phone_book)
                    print(f'\nКонтакт {contact} успешно сохранён!\n')
                case '7':
                    contact = delete_contact(phone_book)
                    print(f'\nКонтакт {contact} успешно удалён!\n')
                case '8':
                    print('До свидания, всего хорошего!')
                    break
                case _:
                    print('Ошибка ввода! Выберите пункт меню от 1 до 8')
    
    except Exception as error:
        logging.warning(f'Произошла ошибка при выполнении кода: {error}')


if __name__ == '__main__':
    main()
