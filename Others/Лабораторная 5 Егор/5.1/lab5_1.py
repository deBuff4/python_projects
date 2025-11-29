class Book:

    title = None
    author = None
    year = None

    def get_info(self):
        print(f"Назваание книги: {self.title}, Автор: {self.author}, Год издание: {self.year}")

Book1 = Book()
Book1.title = "Война и мир"
Book1.author = "Л. Н. Толстой"
Book1.year = 1869
Book1.get_info()