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
    def __init__(self, title, description="", status="Pending", priority=3):
        self.id = ...
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
        return f"Task: {self.title} status: {self.STATUSES_LOC[self.__status]}"


class TaskManager:
    def __init__(self):
        self._tasks = []

    def add_task(self, new_task: Task):
        ...

    def view_tasks(self) -> None:
        ...


if __name__ == "__main__":
    # task_manager = TaskManager()
    task1 = Task("Купить продукты", "Молоко, хлеб, сыр...", status="Bad")
    task1.status = Task.COMPLETED
    print(task1)
    # task1.status = Task.COMPLETED
    # task_manager.add_task(task1)
