from find_contact import find_contact
from show_contacts import show_contacts

def delete_contact(pb: dict) -> str:
    result = find_contact(pb)
    show_contacts(result)
    uid = int(input('Введите ID контакта, который хотите удалить: '))
    c_name, _, _ = pb[uid]
    pb = pb.pop(uid)
    return c_name

def main():
    contact = delete_contact({1: ['Test', 'Tel', 'Text']})
    print(f'\nКонтакт {contact} успешно сохранён!\n')

if __name__ == '__main__':
    main()
