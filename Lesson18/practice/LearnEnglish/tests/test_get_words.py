import pytest
import sqlite3
from pathlib import Path

# Импортируем функции из вашего файла с кодом
from database import init_db, add_word, get_all_words, Connect



@pytest.fixture
def in_memory_cursor():
    """
    Фикстура Pytest, которая создает и инициализирует
    соединение с базой данных SQLite в памяти,
    и возвращает курсор для этого соединения.
    Гарантирует, что таблица 'words' существует и соединение
    корректно закрывается после теста.
    """
    db_path = Path(":memory:")  # Специальное имя для in-memory БД
    conn = None
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Инициализируем таблицу 'words'
        init_db(cursor)

        yield cursor  # Возвращаем курсор для использования в тестах

    finally:
        # Этот блок выполняется после завершения каждого теста
        if conn:
            conn.commit()  # Сохраняем все изменения, сделанные в тесте
            conn.close()  # Закрываем соединение, уничтожая in-memory БД


def test_get_words_empty_dictionary(in_memory_cursor, capsys):
    """
    Тест: Проверяет, что get_words возвращает пустой словарь и выводит сообщение,
    когда словарь пуст.
    """
    words = get_all_words(in_memory_cursor)

    assert words == [], "Функция должна возвращать пустой список при отсутствии слов."


def test_get_words_single_word(in_memory_cursor, capsys):
    """
    Тест: Проверяет, что get_words корректно извлекает одно слово.
    """
    add_word(in_memory_cursor, "cat", "кошка")
    words = get_all_words(in_memory_cursor)

    assert words == [("cat", "кошка")], "Функция должна вернуть список с одним словом."


def test_get_words_multiple_words(in_memory_cursor, capsys):
    """
    Тест: Проверяет, что get_words корректно извлекает несколько слов.
    """
    add_word(in_memory_cursor, "zebra", "зебра")
    add_word(in_memory_cursor, "apple", "яблоко")
    add_word(in_memory_cursor, "dog", "собака")

    words = get_all_words(in_memory_cursor)

    expected_words = [
        ("zebra", "зебра"),
        ("apple", "яблоко"),
        ("dog", "собака")
    ]

    assert words == expected_words, "Функция должна вернуть список со всеми добавленными словами."

