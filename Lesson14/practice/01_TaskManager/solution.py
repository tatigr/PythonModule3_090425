import sqlite3


def create_table(path_to_db):
    connect = sqlite3.connect(path_to_db)
    cursor = connect.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS tasks (
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT DEFAULT 'Pending' CHECK (status IN ('Pending', 'In Progress', 'Completed')),
        priority INTEGER DEFAULT 3 CHECK (priority >= 1 AND priority <= 5)
    );
    """

    cursor.execute(sql)
    connect.commit()

    cursor.close()
    connect.close()


def insert_task(path_to_db, title, description=None, status='Pending', priority=3):
    connect = sqlite3.connect(path_to_db)
    cursor = connect.cursor()

    sql = """
    INSERT INTO tasks (title, description, status, priority)
    VALUES (?, ?, ?, ?); 
    """

    cursor.execute(sql, (title, description, status, priority))
    connect.commit()

    cursor.close()
    connect.close()


def get_tasks(path_to_db, sql) -> list:
    connect = sqlite3.connect(path_to_db)
    cursor = connect.cursor()

    cursor.execute(sql)
    data = cursor.fetchall()

    cursor.close()
    connect.close()
    return data


if __name__ == "__main__":
    create_table('tasks.db')
    # insert_task(path_to_db='tasks.db', title="Позвонить другу", priority=5)
    # insert_task(path_to_db='tasks.db', title="Необязательная задача", priority=1)
    # insert_task(path_to_db='tasks.db', title="Проверка кода", description="Протестировать работу функции")
    # insert_task(path_to_db='tasks.db', title="Протестировать код")
    # insert_task(path_to_db='tasks.db', title="Закодировать логику")

    # Получить все столбцы для всех задач в таблице.
    # sql = """
    # SELECT * FROM tasks;
    # """

    # Задача без описания, но с **высоким приоритетом (5)**, статусом "В ожидании" и названием "Позвонить другу".
    # sql = """
    # SELECT * FROM tasks
    # WHERE description IS NULL AND priority = 1 AND status = "Pending";
    # """

    # Получаем задачи, в которых присутствует "код"
    sql = """
    SELECT title, priority FROM tasks
    WHERE title LIKE '%код%';
    """
    tasks = get_tasks('tasks.db', sql)
    for task in tasks:
        print(task)
