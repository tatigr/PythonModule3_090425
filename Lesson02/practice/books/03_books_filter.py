class Author:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def short_name(self) -> str:
        return f"{self.name[0]}.{self.surname}"


class Book:
    def __init__(self, name: str, author: Author, year: int, pages: int):
        self.name = name
        self.author = author
        self.year = year
        self.pages = pages

    def to_str(self) -> str:
        return f'"{self.name}" author:{self.author.short_name()} publish:{self.year} год'


author1 = Author("Михаил", "Булгаков")
author2 = Author(name="Стивен", surname="Кинг")

books_catalog = [
    Book("Вьюга", author1, 1926, 25),
    Book("Мастер и Маргарита", author1, 1967, 480),
    Book("Собачье сердце", author1, 1987, 352),
    Book("Сияние", author2, 2014, 544),
    Book("Оно", author2, 1986, 320),
]

print("Найти все книги по фамилии автора")
surname = input("Фамилия автора: ")

# Вариант-1
# i = 0
# for book in books_catalog:
#     if book.author.surname == surname:
#         i += 1
#         print(f"{i}. {book.to_str()}")
#
# # if not i:
# if i == 0:
#     print(f"Книг автора {surname} не найдено.")

# Вариант-2 
try:
    matched_books = [book for book in books_catalog if book.author.surname.lower() == surname.lower()]
    if not matched_books:
        raise ValueError
    for i, book in enumerate(matched_books, 1):
        print(f"{i}. {book.to_str()}")
except ValueError:
    print(f"Книг автора {surname} не найдено.")
