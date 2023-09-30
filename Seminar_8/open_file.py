def open_file(path: str = 'phones.txt') -> dict:
    phone_book = {}    
    
    with open(path, 'r', encoding='UTF-8') as file:
        contacts = file.readlines()
    
    for i, contact in enumerate(contacts, 1):
        phone_book[i] = contact.strip().split(';')
    
    return phone_book


def main():
    phone_book = open_file()
    print(phone_book)

if __name__ == '__main__':
    main()
