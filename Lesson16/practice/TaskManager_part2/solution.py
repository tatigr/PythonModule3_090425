from connection import Connect
from pathlib import Path
from typing import Optional


class Task:
    # TODO-0: используйте результат предыдущего занятия
    #  следуя принципам SPR, разбейте класс на два:
    #  1. класс Task будет содержать только данные задачи и базовые методы для представления.
    #  2. класс TaskRepository будет отвечать за все операции с базой данных: создание таблицы, сохранение...
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    def __init__(self, title, description="", status="Pending", priority=3):
        self.id = None
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority

    def __repr__(self):
        # TODO-1[complete]: Возвращает строку формата Task(id=..., title='...', priority=...)
        return f"Task(id={self.id}, title='{self.title}', priority='{self.priority}')"

# sqlite3
class TaskRepository:
    DB_FILE = Path("tasks.db")
    @classmethod
    def _ensure_db_table_exists(cls) -> None:
        """Создает таблицу tasks, если она еще не существует."""
        # cls.DB_FILE.parent.mkdir(parents=True, exist_ok=True)  # Убедимся, что директория существует
        with Connect(cls.DB_FILE) as cursor:
            cursor.execute('''
                    CREATE TABLE IF NOT EXISTS tasks
                    (
                        task_id     INTEGER PRIMARY KEY AUTOINCREMENT,
                        title       TEXT NOT NULL,
                        description TEXT,
                        status      TEXT CHECK (status IN ('Pending', 'In Progress', 'Completed')) DEFAULT 'Pending',
                        priority    INTEGER CHECK ( priority BETWEEN 1 AND 5) DEFAULT 3
                    );
                ''')
        # commit() происходит автоматически при выходе из with Connect

    def save(self, task: Task) -> None:
        """
        Сохраняет или обновляет задачу в базе данных.
        Если id None, вставляет новую задачу. Иначе, обновляет существующую.
        """
        # TODO-2[complete]: реализуйте метод
        Task._ensure_db_table_exists()
        sql_insert = "INSERT INTO tasks (title, description, status, priority) VALUES (?, ?, ?, ?)"
        sql_update = """
        UPDATE tasks
        SET title = ?, description = ?, status = ?, priority = ?
        WHERE task_id = ?
        """
        if task.id is None: # Задачи нет в БД
            with Connect(self.DB_FILE) as cursor:
                cursor.execute(sql_insert, (task.title, task.description, task.status, task.priority))
                task.id = cursor.lastrowid
        else:
            with Connect(self.DB_FILE) as cursor:
                cursor.execute(sql_update, (task.title, task.description, task.status, task.priority, task.id))

    @classmethod
    def get_by_id(cls, task_id: int) -> Task | None:
        # TODO-4: реализуйте метод
        sql_select = "SELECT * FROM tasks WHERE task_id = ?"
        with Connect(cls.DB_FILE) as cursor:
            cursor.execute(sql_select, (task_id, ))
            task_data = cursor.fetchone()

        if task_data is None:
            print(f"Задача с id={task_id} не найдена")
            return None

        task = Task(*task_data[1:])
        task.id = task_data[0]
        return task

    def delete(self, task) -> None:
        """Удаляет задачу из базы данных."""
        # TODO-3[Complete]: реализуйте метод
        if task.id is None:
            print("Нельзя удалить несохраненную задачу")
            return
        sql_delete = "DELETE FROM tasks WHERE task_id = ?"
        with Connect(self.DB_FILE) as cursor:
            cursor.execute(sql_delete, (task.id, ))
            task.id = None

# Использование
task_repository = TaskRepository() # Создаем экземпляр репозитория

# Создаем новую задачу
new_task = Task("Купить молоко", "Зайти в магазин", priority=1)
task_repository.save(new_task) # Сохраняем новую задачу, new_task.id будет обновлен
# print(f"Сохранена новая задача: {new_task}")

# Получаем задачу по ID
retrieved_task = task_repository.get_by_id(new_task.id)
if retrieved_task:
    print(f"Получена задача: {retrieved_task}")
    retrieved_task.description = "Купить 2 литра молока"
    retrieved_task.mark_as_in_progress()
    task_repository.save(retrieved_task) # Обновляем задачу
    print(f"Обновленная задача: {retrieved_task}")

# Получаем все задачи
all_tasks = task_repository.get_all_tasks()
print("\nВсе задачи:")
for task in all_tasks:
    print(task)

# Удаляем задачу
if retrieved_task:
    task_repository.delete(retrieved_task)
    print(task_repository.get_by_id(retrieved_task.id)) # Должно быть None