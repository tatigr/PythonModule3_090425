CREATE TABLE IF NOT EXISTS words
(
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    english_word        TEXT NOT NULL UNIQUE,
    russian_translation TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS answers
(
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    word_id    INTEGER NOT NULL,
    timestamp  TEXT    NOT NULL,
    is_correct INTEGER NOT NULL,
    FOREIGN KEY (word_id) REFERENCES words (id) ON DELETE CASCADE
);