from src.usecase.interfaces import DBInterface
from src.entity.task import Task


class TaskUsecases:
    def __init__(
        self,
        db: DBInterface,
    ) -> None:
        self.db = db

    def add_task(self, task: Task) -> int:
        return self.db.add_task(task.model_dump())

    def get_task(self, task_id: int) -> Task:
        return Task(**self.db.get_task(task_id))

    def complete_task(self, task_id: int) -> None:
        task = self.get_task(task_id)
        task.nextup = task.nextup + task.timedelta
        self.update_task(task_id, task)

    def update_task(self, task_id: int, data: Task) -> None:
        self.db.update_task(task_id, data.model_dump())

    def delete_task(self, task_id: int) -> None:
        self.db.delete_task(task_id)

    def list_tasks(self) -> list[Task]:
        return [Task(**t) for t in self.db.list_tasks()]
