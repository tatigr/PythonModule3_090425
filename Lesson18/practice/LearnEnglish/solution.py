import sqlite3
import random
import database
from helpers.connection import Connect
from pathlib import Path

DATABASE_NAME = Path('vocabulary.db')


def start_test(cursor):
    """Запускает режим тестирования."""
    # 1. Получаем все слова из БД
    all_words = database.get_all_words(cursor)

    random.shuffle(all_words)
    for english_word, correct_translation in all_words:
        user_input = input(f"Как переводится '{english_word}'? (или 'стоп'/'exit' для выхода): ").strip().lower()

        if user_input in ('стоп', 'exit'):
            print("Тест завершен.")
            break

        if user_input == correct_translation:
            print("Верно!")
        else:
            print(f"Неправильно. Правильный перевод: '{correct_translation}'.")

        print("-" * 20)  # Разделитель для следующего вопроса


def main_menu(cursor: sqlite3.Cursor):
    """Главное меню приложения."""
    database.init_db(cursor)
    while True:
        print("\n--- Меню приложения 'Английский для новичков' ---")
        print("1. Добавить слово")
        print("2. Посмотреть слова")
        print("3. Удалить слово")
        print("4. Начать тест")
        print("5. Выход")
        print("-------------------------------------------------")

        choice = input("Выберите действие: ").strip()

        if choice == '1':
            english = input("Введите английское слово: ").strip().lower()
            russian = input("Введите русский перевод: ").strip().lower()
            database.add_word(cursor, english, russian)
        elif choice == '2':
            database.view_words(cursor)
        elif choice == '3':
            english = input("Введите английское слово, которое хотите удалить: ").strip().lower()
            database.delete_word(cursor, english)
        elif choice == '4':
            start_test(cursor)
        elif choice == '5':
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 5.")


if __name__ == "__main__":
    with Connect(DATABASE_NAME) as cursor:
        main_menu(cursor)
