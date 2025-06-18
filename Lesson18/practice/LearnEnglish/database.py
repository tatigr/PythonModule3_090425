import random
import sqlite3
from pathlib import Path
from helpers.connection import Connect


def init_db(cursor):
    """Инициализирует базу данных, создает таблицу words, если ее нет."""
    sql = """
    CREATE TABLE IF NOT EXISTS words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    english_word TEXT NOT NULL UNIQUE,
    russian_translation TEXT NOT NULL
    );
    """
    cursor.execute(sql)


def add_word(cursor, english_word: str, russian_translation: str) -> None:
    """Позволяет пользователю добавить новое слово и перевод."""
    sql = """
    INSERT INTO words (english_word, russian_translation)
    VALUES (?, ?)
    """
    cursor.execute(sql, (english_word, russian_translation))


def get_all_words(cursor) -> list[tuple]:
    sql = """
        SELECT english_word, russian_translation FROM words
        """
    cursor.execute(sql)
    words_data = cursor.fetchall()

    return words_data


def view_words(cursor) -> None:
    """Отображает все слова в словаре."""
    words_data = get_all_words(cursor)

    for word_data in words_data:
        print(word_data)


def delete_word(cursor, english_word: str) -> None:
    """Удаляет слово из словаря по английскому слову."""
    sql = """
    DELETE FROM words WHERE english_word = ?
    """
    cursor.execute(sql, (english_word,))
    word_count = cursor.rowcount

    if word_count > 0:
        print(f"Слово {english_word} удалено")
    else:
        print(f"Слово {english_word} не найдено")


def get_all_tables(cursor: sqlite3.Cursor):
    """Вспомогательная функция для получения списка всех таблиц в БД (для тестов)."""
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return [row[0] for row in cursor.fetchall()]


def get_table_info(cursor: sqlite3.Cursor, table_name: str):
    """Вспомогательная функция для получения информации о таблице (для тестов)."""
    cursor.execute(f"PRAGMA table_info({table_name})")
    return cursor.fetchall()