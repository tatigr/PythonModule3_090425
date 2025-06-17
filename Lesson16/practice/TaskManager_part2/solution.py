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
        self.__priority = priority

    @property
    def priority(self):
        return self.__priority

    @staticmethod
    def _convert_data_to_task(task_data: tuple) -> 'Task':
        task = Task(*task_data[1:])
        task.id = task_data[0]
        return task

    def mark_as_completed(self):
        self.status = Task.COMPLETED

    def mark_as_pending(self):
        self.status = Task.PENDING

    def mark_as_in_progress(self):
        self.status = Task.IN_PROGRESS

    def set_priority(self, new_priority):
        if 1 <= new_priority <= 5:
            self.__priority = new_priority
        else:
            raise ValueError("The priority must be in the range from 1 to 5")

    def __repr__(self):
        return f"Task(id={self.id}, title='{self.title}', status='{self.status}' priority='{self.__priority}')"


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
        TaskRepository._ensure_db_table_exists()
        sql_insert = "INSERT INTO tasks (title, description, status, priority) VALUES (?, ?, ?, ?)"
        sql_update = """
        UPDATE tasks
        SET title = ?, description = ?, status = ?, priority = ?
        WHERE task_id = ?
        """
        if task.id is None:  # Задачи нет в БД
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
            cursor.execute(sql_select, (task_id,))
            task_data = cursor.fetchone()

        if task_data is None:
            print(f"Задача с id={task_id} не найдена")
            return None

        return Task._convert_data_to_task(task_data)

    @classmethod
    def _get_task_by_attribute(cls, attr_name: str, attr_value: str):
        sql = f"""
                SELECT * FROM tasks
                WHERE {attr_name} = ?;
                """
        with Connect(cls.DB_FILE) as cursor:
            cursor.execute(sql, (attr_value,))
            tasks_data = cursor.fetchall()

        return list(map(Task._convert_data_to_task, tasks_data))

    def get_tasks_by_status(self, status: str) -> list[Task]:
        return self._get_task_by_attribute('status', status)

    def get_tasks_by_priority(self, priority: int) -> list[Task]:
        return self._get_task_by_attribute('priority', str(priority))

    def get_completed_tasks(self) -> list[Task]:
        return self._get_task_by_attribute('status', Task.COMPLETED)

    @classmethod
    def get_all_tasks(cls):
        return cls._get_task_by_attribute(1, 1)

    @classmethod
    def delete_completed_tasks(cls) -> None:
        sql = """
        DELETE FROM tasks
        WHERE status = 'Completed'
        """
        with Connect(cls.DB_FILE) as cursor:
            cursor.execute(sql)

    def delete(self, task) -> None:
        """Удаляет задачу из базы данных."""
        # TODO-3[Complete]: реализуйте метод
        if task.id is None:
            print("Нельзя удалить несохраненную задачу")
            return
        sql_delete = "DELETE FROM tasks WHERE task_id = ?"
        with Connect(self.DB_FILE) as cursor:
            cursor.execute(sql_delete, (task.id,))
            task.id = None


# Использование
task_repository = TaskRepository()  # Создаем экземпляр репозитория

# Создаем новую задачу
task1 = Task("Купить молоко -1", priority=1, status=Task.COMPLETED)
task2 = Task("Купить молоко -2", priority=1, status=Task.COMPLETED)
task3 = Task("Купить молоко -3", priority=1, status=Task.IN_PROGRESS)
task4 = Task("Купить молоко -4", priority=1, status=Task.COMPLETED)
task_repository.save(task1)  # Сохраняем новую задачу, new_task.id будет обновлен
task_repository.save(task2)  # Сохраняем новую задачу, new_task.id будет обновлен
task_repository.save(task3)  # Сохраняем новую задачу, new_task.id будет обновлен
task_repository.save(task4)  # Сохраняем новую задачу, new_task.id будет обновлен

tasks = task_repository.get_all_tasks()
for task in tasks:
    print(task)
# print(f"Сохранена новая задача: {new_task}")

# Получаем задачу по ID
# retrieved_task = task_repository.get_by_id(new_task.id)
# if retrieved_task:
#     print(f"Получена задача: {retrieved_task}")
#     retrieved_task.description = "Купить 2 литра молока"
#     retrieved_task.mark_as_in_progress()
#     task_repository.save(retrieved_task)  # Обновляем задачу
#     print(f"Обновленная задача: {retrieved_task}")
#
# # Получаем все задачи
# all_tasks = task_repository.get_all_tasks()
# print("\nВсе задачи:")
# for task in all_tasks:
#     print(task)
#
# # Удаляем задачу
# if retrieved_task:
#     task_repository.delete(retrieved_task)
#     print(task_repository.get_by_id(retrieved_task.id))  # Должно быть None
