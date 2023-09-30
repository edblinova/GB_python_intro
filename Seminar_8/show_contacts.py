def show_contacts(pb: dict) -> None:
    print()
    for i, contact in pb.items():
        print(f'{i:>3}. {contact[0]:<20} {contact[1]:<20} {contact[2]:<20}')
    print()


def main():
    print('\nТелефонная книга:\n')
    show_contacts({1: ['Test', 'Tel', 'Text']})

if __name__ == '__main__':
    main()
