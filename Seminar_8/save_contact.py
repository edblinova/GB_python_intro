def save_contact(pb: dict) -> str:
    name = input('Введите имя контакта: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    uid = max(pb.keys())+1
    pb[uid] = [name, phone, comment]
    return name


def main():
    contact = save_contact({1: ['Test', 'Tel', 'Text']})
    print(f'\nКонтакт {contact} успешно сохранён!\n')

if __name__ == '__main__':
    main()
