from src.typing import StrDict
from src.usecase.interfaces import DBInterface


class TaskUsecases:
    def __init__(
        self,
        db: DBInterface,
    ) -> None:
        self.db = db

    def add_task(self, task: StrDict) -> None:
        self.db.add_task(task)

    def get_task(self, task_id: int) -> StrDict:
        return self.db.get_task(task_id)

    def update_task(self, task_id: int, data: StrDict) -> None:
        self.db.update_task(task_id, data)

    def delete_task(self, task_id: int) -> None:
        self.db.delete_task(task_id)

    def list_tasks(self) -> list[StrDict]:
        return self.db.list_tasks()
