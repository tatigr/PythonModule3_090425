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
    sql_answers = """
    CREATE TABLE IF NOT EXISTS answers(
        id         INTEGER PRIMARY KEY AUTOINCREMENT,
        word_id    INTEGER NOT NULL,
        timestamp  TEXT    NOT NULL,
        is_correct INTEGER NOT NULL,
        FOREIGN KEY (word_id) REFERENCES words (id) ON DELETE CASCADE
    );
    """
    cursor.execute(sql)
    cursor.execute(sql_answers)


def add_word(cursor, english_word: str, russian_translation: str) -> None:
    """Позволяет пользователю добавить новое слово и перевод."""
    sql = """
    INSERT INTO words (english_word, russian_translation)
    VALUES (?, ?)
    """
    if not english_word or not russian_translation:
        raise ValueError("Слово или перевод не должны быть пустыми")
    cursor.execute(sql, (english_word, russian_translation))


def get_all_words(cursor) -> list[tuple]:
    sql = """
        SELECT id, english_word, russian_translation FROM words
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


def record_answer(cursor: sqlite3.Cursor, word_id: int, timestamp: str, is_correct: int) -> None:
    sql = """
    INSERT INTO answers (word_id, timestamp, is_correct)
    VALUES (?, ?, ?);
    """
    cursor.execute(sql, (word_id, timestamp, is_correct))


def get_words_stats(cursor: sqlite3.Cursor) -> list[dict]:
    sql = """
    SELECT 
       words.id,
       words.english_word,
       words.russian_translation,
       COUNT(answers.id)                                       AS total_questions,
       SUM(CASE WHEN answers.is_correct = 1 THEN 1 ELSE 0 END) AS correct_answers,
       SUM(CASE WHEN answers.is_correct = 0 THEN 1 ELSE 0 END) AS incorrect_answers
    FROM words
         JOIN answers ON words.id = answers.word_id
    GROUP BY words.id;
    """
    # word = {
    #     "english_word": ...,
    #     "total_questions": ...,
    #     "correct_answers": ...,
    #     "incorrect_answers": ...,
    # }
    words: list[dict] = []
    keys = ["word_id", "english_word", "russian_translation", "total_questions", "correct_answers", "incorrect_answers"]
    cursor.execute(sql)
    words_data: list[tuple] = cursor.fetchall()

    for word_data in words_data:
        word: dict = dict(zip(keys, word_data))
        word["incorrect_percent"] = word["incorrect_answers"] / word["total_questions"]
        words.append(word)

    return words


if __name__ == "__main__":
    with Connect(Path('vocabulary.db')) as cursor:
        result = get_words_stats(cursor)
        print(result)
