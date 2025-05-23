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


author = Author("Михаил", "Булгаков")
book = Book("Вьюга", author, 1926, 25)

# TODO-3: Измените имя, фамилию автора и название книги, проверьте, что программа корректно работает с новыми значениями
author.surname = "Иванов"
print(book.to_str())
