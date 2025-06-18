import random
import sqlite3
from pathlib import Path
from helpers.connection import Connect

DATABASE_NAME = 'vocabulary.db'


def init_db():
    """Инициализирует базу данных, создает таблицу words, если ее нет."""
    sql = """
    CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    english_word TEXT NOT NULL UNIQUE,
    russian_translation TEXT NOT NULL
    );
    """
    with Connect(Path(DATABASE_NAME)) as cursor:
        cursor.execute(sql)


def add_word(english_word: str, russian_translation: str) -> None:
    """Позволяет пользователю добавить новое слово и перевод."""
    sql = """
    INSERT INTO words (english_word, russian_translation)
    VALUES (?, ?)
    """
    with Connect(Path(DATABASE_NAME)) as cursor:
        cursor.execute(sql, (english_word, russian_translation))


def get_all_words() -> list[tuple]:
    sql = """
        SELECT english_word, russian_translation FROM words
        """
    with Connect(Path(DATABASE_NAME)) as cursor:
        cursor.execute(sql)
        words_data = cursor.fetchall()

    return words_data


def view_words() -> None:
    """Отображает все слова в словаре."""
    words_data = get_all_words()

    for word_data in words_data:
        print(word_data)


def delete_word(english_word: str) -> None:
    """Удаляет слово из словаря по английскому слову."""
    sql = """
    DELETE FROM words WHERE english_word = ?
    """
    with Connect(Path(DATABASE_NAME)) as cursor:
        cursor.execute(sql, (english_word,))
        word_count = cursor.rowcount

    if word_count > 0:
        print(f"Слово {english_word} удалено")
    else:
        print(f"Слово {english_word} не найдено")
