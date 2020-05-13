class Book:

    total_number_of_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_number_of_books += 1
        self.id = Book.total_number_of_books


if __name__ == '__main__':
    nad_niemnem = Book('Nad Niemnem', 'Eliza Orzeszkowa')
    print(Book.total_number_of_books)
    print(nad_niemnem.id)

    pan_tadeusz = Book('Pan Tadeusz', 'Adam Mickiewicz')
    print(Book.total_number_of_books)
    print(pan_tadeusz.id)
