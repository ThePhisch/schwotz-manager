from typing import Generator

from src.usecase.generic import Usecase
from src.usecase.interfaces import DBInterface
from src.entity.task import Task
from src.typing import StrDict


class TaskDBInterface(DBInterface):
    def add_task(self, task: StrDict) -> int: ...

    def get_task(self, task_id: int) -> StrDict: ...

    def update_task(self, task_id: int, data: StrDict) -> None: ...

    def delete_task(self, task_id: int) -> None: ...

    def list_tasks(self) -> Generator[StrDict, None, None]: ...


class TaskUsecases(Usecase[TaskDBInterface]):

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
