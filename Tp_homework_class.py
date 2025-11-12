class Book:
    def __init__(self, title, author, year):
        self.__title = title
        self.__author = author
        self.__year = year
        self.__available = True

    def get_title(self):
        return self.__title
    def get_author(self):
        return self.__author
    def get_year(self):
        return self.__year
    def is_available(self):
        return self.__available

    def mark_as_taken(self):
        self.__available = False
    def mark_as_returned(self):
        self.__available = True

    def __str__(self):
        return f"Книга: '{self.__title}', автор: {self.__author}, год: {self.__year}, статус: {self.__available}"

class PrintedBook(Book):
    def __init__(self, title, author, year, pages, condition):
        super().__init__(title, author, year)
        self.pages = pages
        self.condition = condition
    def repair(self):
        if self.condition == 'плохая':
            self.condition = 'хорошая'
        else:
            self.condition = 'новая'

class EBook(Book):
    def __init__(self, title, author, year, file_size: int, b_format):
        super().__init__(title, author, year)
        self.file_size = file_size
        self.format = b_format

    def download(self):
        print(f'Книга {self.get_title()} загружается...')

class User:
    def __init__(self, name):
        self.name = name
        self.__borrowed_book = []

    def borrow(self, book):
        if book.is_available():
            book.mark_as_taken()
            self.__borrowed_book.append(book)
        else:
            print('книга недоступна')

    def return_book(self, book):
        book.mark_as_returned()
        self.__borrowed_book.remove(book)

    def show_books(self):
        return self.__borrowed_book

    def get_borrowed_books(self):
        return tuple(self.__borrowed_book)

class Librarian(User):
    def __init__(self, name):
        super().__init__(name)
    def add_book(self, library, book):
        library.add_book(book)
    def remove_book(self, library, title):
        library.remove_book(title)
    def register_user(self, library, user):
        library.add_user(user)

class Library:
    def __init__(self):
        self.__books = []
        self.__users = []

    def add_book(self, book):
        self.__books.append(book)
    def remove_book(self, title):
        self.__books = [b for b in self.__books if b.get_title() == title]
    def add_user(self, user):
        self.__users.append(user)
    def find_book(self, title):
        for i in self.__books:
            if i.get_title() == title:
                return i
        return None
    def show_all_books(self):
        print(self.__books)
    def show_available_books(self):
        poop = []
        for i in self.__books:
            if i.is_available():
                poop.append(i)
        return poop
    def lend_book(self, title, user_name):
        book1 = self.find_book(title)
        user1 = [i for i in self.__users if i.name == user_name]
        if book1 and user1:
            user1[0].borrow(book1)

    def return_book(self, title, user_name):
        book1 = self.find_book(title)
        user1 = [i for i in self.__users if i.name == user_name]
        if book1 and user1:
            user1[0].return_book(book1)




# --- создаём библиотеку ---
lib = Library()
# --- создаём книги ---
b1 = PrintedBook("Война и мир", "Толстой", 1869, 1225, "хорошая")
b2 = EBook("Мастер и Маргарита", "Булгаков", 1966, 5, "epub")
b3 = PrintedBook("Преступление и наказание", "Достоевский", 1866, 480,
"плохая")
# --- создаём пользователей ---
user1 = User("Анна")
librarian = Librarian("Мария")
# --- библиотекарь добавляет книги ---
librarian.add_book(lib, b1)
librarian.add_book(lib, b2)
librarian.add_book(lib, b3)
# --- библиотекарь регистрирует пользователя ---
librarian.register_user(lib, user1)
# --- пользователь берёт книгу ---
lib.lend_book("Война и мир", "Анна")
# --- пользователь смотрит свои книги ---
user1.show_books()
# --- возвращает книгу ---
lib.return_book("Война и мир", "Анна")
# --- электронная книга ---
b2.download()
# --- ремонт книги ---
b3.repair()
print(b3)