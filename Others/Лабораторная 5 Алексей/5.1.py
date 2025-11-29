class book:
    title = ''
    author = ''
    year = ''
    def get_info(self):
        return 'Название книги: ' + self.title + ', Автор: ' + self.author + ', Год издания: ' + self.year + '.'
Book = book()
Book.title = 'house of leaves'
Book.author = 'Mark Z. Danielewski'
Book.year = 'March 7, 2000'
print(Book.get_info())