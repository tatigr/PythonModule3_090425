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
    def __init__(self,id, title, description="", status="Pending", priority=3):
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


class TaskManager:
    def __init__(self):
        self._tasks = []
        self._next_task_id = 1

    def add_task(self, title, description="", status="Pending", priority=3):
        new_task = Task(self._next_task_id, title, description, status, priority)
        self._next_task_id += 1
        self._tasks.append(new_task)

    def view_tasks(self) -> None:
        for task in self._tasks:
            print(task)


if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.add_task("Купить продукты", "Молоко, хлеб, сыр...")
    task_manager.add_task("Проверить работу класс", "Тестирование кода")

    task_manager.view_tasks()

