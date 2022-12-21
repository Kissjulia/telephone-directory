import view

phone_book = []

def get_phone_book() -> list:
    global phone_book
    return phone_book

def set_phone_book(new_phone_book: list):
    global phone_book
    phone_book = new_phone_book

def add_contact():
    global phone_book
    contact = view.input_new_contact()
    phone_book.append(contact)

def remove_contact():
    global phone_book
    id = view.input_remove_contact()
    confirm = input(f'Вы точно хотите удалить контакт {phone_book[id-1][0]}? (y/n)')
    if confirm.lower() == 'y':
        del_contact = phone_book.pop(id-1)

def change_contact():
    global phone_book
    id = view.input_change_contact()
    confirm = input(f'Вы точно хотите изменить контакт {phone_book[id-1][0]}? (y/n)')
    if confirm.lower() == 'y':
        change_contact = phone_book.pop(id-1)
        contact = view.input_new_contact()
        phone_book.append(contact)

def search_contact():
    global phone_book
    id = view.input_search_contact()
    if id in phone_book:
            print(id)
