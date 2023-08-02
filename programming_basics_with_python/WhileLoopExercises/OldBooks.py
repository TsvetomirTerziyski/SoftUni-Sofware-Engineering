book_name = input()

book_counter = 0

while True:
    book = input()

    book_counter += 1

    if book == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {book_counter-1} books.')
        break

    if book == book_name:
        print(f'You checked {book_counter-1} books and found it.')
        break