import sqlite3

import pytest
from database import init_db, get_all_tables, get_table_info, add_word
from helpers.connection import Connect
from pathlib import Path


@pytest.fixture
def db_cursor():
    with Connect(Path(":memory:")) as cursor:
        yield cursor


def test_successful_add(db_cursor):
    init_db(db_cursor)
    add_word(db_cursor, "apple", "яблоко")
    db_cursor.execute("SELECT english_word, russian_translation FROM words")
    rows = db_cursor.fetchall()
    assert ("apple", "яблоко") in rows


def test_raise_unique_duplicate(db_cursor):
    init_db(db_cursor)
    add_word(db_cursor, "apple", "яблоко")
    with pytest.raises(sqlite3.IntegrityError):
        add_word(db_cursor, "apple", "яблоко")