import pytest
from database import init_db, get_all_tables, get_table_info
from helpers.connection import Connect
from pathlib import Path

@pytest.fixture
def db_cursor():
    with Connect(Path(":memory:")) as cursor:
        yield cursor

def test_create_table(db_cursor):
    # Тестовая БД
    # 1.  Создаем БД (memory)
    # 2.  Создаем таблицу (используя init_db)
    # 3.  Проверяем что таблица с нудными полями есть в БД
    # 4.  Удаляем БД
    init_db(db_cursor)
    tables = get_all_tables(db_cursor)
    assert 'words' in tables


def test_create_table_with_columns(db_cursor):
    init_db(db_cursor)
    table_info = get_table_info(db_cursor, "words")

    column_names = [col[1] for col in table_info]
    column_types = {col[1]: col[2] for col in table_info}

    assert 'id' in column_names
    assert 'english_word' in column_names
    assert 'russian_translation' in column_names

    assert column_types['id'] == 'INTEGER'
    assert column_types['english_word'] == 'TEXT'
    assert column_types['russian_translation'] == 'TEXT'



