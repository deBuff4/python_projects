class Book:
    title = ''
    author = ''
    year = ''
    def get_info(self):
        return 'Название книги: ' + self.title + ', Автор: ' + self.author + ', Год издания: ' + self.year + '.'
book = Book()
book.title = 'house of leaves'
book.author = 'Mark Z. Danielewski'
book.year = 'March 7, 2000'
print(book.get_info())