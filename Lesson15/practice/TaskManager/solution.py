from connection import Connect
from pathlib import Path
from typing import Optional


class Task:
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

    DB_FILE = Path("tasks.db")

    def __init__(self, title, description="", status="Pending", priority=3):
        # TODO-0: что будем делать с id?
        self.id = None
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority

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

    def __repr__(self):
        # TODO-1[complete]: Возвращает строку формата Task(id=..., title='...', priority=...)
        return f"Task(id={self.id}, title='{self.title}', priority='{self.priority}')"

    def save(self) -> None:
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
        if self.id is None: # Задачи нет в БД
            with Connect(self.DB_FILE) as cursor:
                cursor.execute(sql_insert, (self.title, self.description, self.status, self.priority))
                self.id = cursor.lastrowid
        else:
            with Connect(self.DB_FILE) as cursor:
                cursor.execute(sql_update, (self.title, self.description, self.status, self.priority, self.id))


    @classmethod
    def get_by_id(cls, task_id: int) -> Optional['Task']:
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

    def delete(self) -> None:
        """Удаляет задачу из базы данных."""
        # TODO-3[Complete]: реализуйте метод
        if self.id is None:
            print("Нельзя удалить несохраненную задачу")
            return
        sql_delete = "DELETE FROM tasks WHERE task_id = ?"
        with Connect(self.DB_FILE) as cursor:
            cursor.execute(sql_delete, (self.id, ))
            self.id = None


if __name__ == "__main__":
    task4 = Task.get_by_id(14)
    print(task4)
    # task1 = Task(title="тестовая задача на удаление")
    # task1.save()
    # input()
    # task1.delete()
    # task1.delete()
    # task1.delete()
