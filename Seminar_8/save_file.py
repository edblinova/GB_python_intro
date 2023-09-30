def save_file(pb: dict = {}, path: str = 'phones.txt') -> None:
    data = []
    for contact in pb.values():
        contact = ';'.join(contact)
        data.append(contact)
    data = '\n'.join(data)
    with open(path, 'w', encoding='UTF-8') as file:
        file.write(data)


def main():
    save_file({1: ['Test', 'Tel', 'Text']})
    print('\nТелефонная книга успешно сохранена!\n')

if __name__ == '__main__':
    main()
