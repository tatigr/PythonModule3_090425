import pytest
import sqlite3
from pathlib import Path

# Импортируем только нужные функции из вашего файла с кодом
from database import init_db, add_word, Connect

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
        init_db(cursor)  # Используем init_db для создания таблицы

        yield cursor  # Возвращаем курсор для использования в тестах

    finally:
        # Этот блок выполняется после завершения каждого теста
        if conn:
            conn.commit()  # Сохраняем все изменения, сделанные в тесте
            conn.close()  # Закрываем соединение, уничтожая in-memory БД


def test_add_word_success(in_memory_cursor):
    """
    Тест: Успешное добавление нового слова в БД.
    """
    # Получаем начальное количество слов напрямую через курсор
    in_memory_cursor.execute("SELECT COUNT(*) FROM words")
    initial_count = in_memory_cursor.fetchone()[0]

    english = "apple"
    russian = "яблоко"
    add_word(in_memory_cursor, english, russian)

    # Проверяем, что слово добавлено и его перевод корректен напрямую через курсор
    in_memory_cursor.execute("SELECT russian_translation FROM words WHERE english_word = ?", (english,))
    retrieved_translation = in_memory_cursor.fetchone()
    assert retrieved_translation is not None and retrieved_translation[0] == russian

    # Проверяем, что количество слов увеличилось на 1 напрямую через курсор
    in_memory_cursor.execute("SELECT COUNT(*) FROM words")
    assert in_memory_cursor.fetchone()[0] == initial_count + 1


def test_add_word_duplicate_entry_raises_error(in_memory_cursor):
    """
    Тест: Попытка добавить дубликат слова должна вызвать ValueError.
    """
    english = "banana"
    russian = "банан"
    add_word(in_memory_cursor, english, russian)  # Добавляем слово один раз

    # Попытка добавить то же слово еще раз (другой перевод не важен)
    with pytest.raises(sqlite3.IntegrityError):
        add_word(in_memory_cursor, english, "фрукт")

    in_memory_cursor.execute("SELECT COUNT(*) FROM words")
    assert in_memory_cursor.fetchone()[0] == 1  # Предполагая, что это было первое и единственное слово


def test_add_word_empty_english_word_raises_error(in_memory_cursor):
    """
    Тест: Добавление слова с пустым английским словом должно вызвать ValueError.
    """
    with pytest.raises(ValueError):
        add_word(in_memory_cursor, "", "пустой")
    # Проверяем, что слово не было добавлено
    in_memory_cursor.execute("SELECT COUNT(*) FROM words")
    assert in_memory_cursor.fetchone()[0] == 0


def test_add_word_empty_russian_translation_raises_error(in_memory_cursor):
    """
    Тест: Добавление слова с пустым русским переводом должно вызвать ValueError.
    """
    with pytest.raises(ValueError):
        add_word(in_memory_cursor, "empty", "")
    # Проверяем, что слово не было добавлено
    in_memory_cursor.execute("SELECT COUNT(*) FROM words")
    assert in_memory_cursor.fetchone()[0] == 0

