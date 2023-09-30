from find_contact import find_contact
from show_contacts import show_contacts

def change_contact(pb: dict) -> str:
    result = find_contact(pb)
    show_contacts(result)
    uid = int(input('Введите ID контакта, который хотите изменить: '))
    c_name, c_phone, c_comment = pb[uid]
    new_name = input('Введите новое имя контакта: ')
    new_phone = input('Введите новый телефон: ')
    new_comment = input('Введите новый комментарий: ')
    pb[uid] = [new_name if new_name else c_name, 
               new_phone if new_phone else c_phone, 
               new_comment if new_comment else c_comment]
    return new_name if new_name else c_name

def main():
    contact = change_contact({1: ['Test', 'Tel', 'Text']})
    print(f'\nКонтакт {contact} успешно сохранён!\n')

if __name__ == '__main__':
    main()
