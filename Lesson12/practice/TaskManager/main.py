import json
from pathlib import Path


# save:  task -> dict -> json  | Сериализация
# load: json -> dict -> task   | Десериализация

class Task:
    PENDING = 'Pending'
    PROCESS = 'In Progress'
    COMPLETED = 'Completed'
    STATUSES = [PENDING, PROCESS, COMPLETED]
    STATUSES_LOC = {
        PENDING: 'В ожидании',
        PROCESS: 'В процессе',
        COMPLETED: 'Завершено',
    }

    # DRY
    def __init__(self, id, title, description="", status="Pending", priority=3):
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.priority = priority

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new_status):
        if new_status not in self.STATUSES:
            raise ValueError("Incorrect status")
        self.__status = new_status

    def __repr__(self):
        return f"Task[{self.id}]: {self.title} status: {self.STATUSES_LOC[self.__status]}"

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "priority": self.priority,
        }


class TaskManager:
    FILE_NAME = "tasks.json"

    def __init__(self):
        self._tasks: list[Task] = []
        self._next_task_id = 1
        self._load_from_file()

    def add_task(self, title, description="", status="Pending", priority=3):
        new_task = Task(self._next_task_id, title, description, status, priority)
        self._next_task_id += 1
        self._tasks.append(new_task)

    def get_task_by_id(self, task_id: int) -> Task | None:
        ...

    def view_tasks(self) -> None:
        for task in self._tasks:
            print(task)

    def _convert_task_dict(self) -> list[dict]:
        tasks_as_dict: list[dict] = []
        for task in self._tasks:
            tasks_as_dict.append(task.to_dict())
        return tasks_as_dict

    def save_to_file(self):
        with open(self.FILE_NAME, "w", encoding="UTF-8") as file:
            json.dump(self._convert_task_dict(), file, ensure_ascii=False)

    def _load_from_file(self):
        self._tasks = []
        with open(self.FILE_NAME, "r", encoding="UTF-8") as file:
            tasks_as_dict = json.load(file)
            for task_as_dict in tasks_as_dict:
                task = Task(**task_as_dict)
                self._tasks.append(task)
                # TODO: после загрузки self._next_task_id установить в корректное значение


if __name__ == "__main__":
    task_manager = TaskManager()
    # task_manager.add_task("Купить продукты", "Молоко, хлеб, сыр...")
    # task_manager.add_task("Проверить работу класс", "Тестирование кода")
    #
    # task_manager.save_to_file()
    # task_manager.add_task("Еще одна задача", "Для проверки")
    # task_manager.view_tasks()

    print("--------------------")
    task_manager.view_tasks()
