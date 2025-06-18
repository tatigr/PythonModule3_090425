import sqlite3
import random
from datetime import datetime, timedelta
from pprint import pprint

def populate_answers(db_name='english_app.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Получаем все слова и их ID из таблицы words
    cursor.execute("SELECT id, english_word FROM words")
    words = cursor.fetchall()

    if not words:
        print("Таблица 'words' пуста. Сначала добавьте слова.")
        return

    answers_to_insert = []
    current_date = datetime.now()

    for word_id, english_word in words:
        num_answers = random.randint(10, 20)  # От 10 до 20 ответов на каждое слово

        for _ in range(num_answers):
            is_correct = random.randint(0, 1)  # 0 для неправильного, 1 для правильного

            # Генерируем случайную дату в пределах последней недели
            days_ago = random.randint(0, 6)  # От 0 до 6 дней назад
            hours_ago = random.randint(0, 23)
            minutes_ago = random.randint(0, 59)
            seconds_ago = random.randint(0, 59)

            answer_time = current_date - timedelta(days=days_ago, hours=hours_ago, minutes=minutes_ago,
                                                   seconds=seconds_ago)
            timestamp = answer_time.strftime('%Y-%m-%d %H:%M:%S')  # Формат ISO 8601

            answers_to_insert.append((word_id, timestamp, is_correct))
    pprint(answers_to_insert)
populate_answers()