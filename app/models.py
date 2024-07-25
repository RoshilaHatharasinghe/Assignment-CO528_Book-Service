books = []

def get_all_books():
    return books

def get_book(book_id):
    return next((book for book in books if book['id'] == book_id), None)

def create_book(data):
    book = {
        'id': len(books) + 1,
        'title': data.get('title'),
        'author': data.get('author'),
        'published': data.get('published')
    }
    books.append(book)
    return book

def update_book(book_id, data):
    book = get_book(book_id)
    if book:
        book.update(data)
        return book
    return None

def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return True
