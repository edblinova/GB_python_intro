from show_contacts import show_contacts

def find_contact(pb: dict) -> dict:
    result = {}
    word = input('Введите ключевое слово для поиска: ').lower()
    for i, contact in pb.items():
        if word in ''.join(contact).lower():
            result[i] = contact
    return result


def main():
    contact = find_contact({1: ['Test', 'Tel', 'Text']})
    show_contacts(contact)

if __name__ == '__main__':
    main()
