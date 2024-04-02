"""
Defines the base interfaces for the usecase layer.

The adapters (e.g. in web, db) will implement these interfaces.
"""

from typing import Protocol
from src.typing import StrDict
from src.entity.task import Task

class DBInterface(Protocol):
    def add_task(self, task: StrDict) -> int: ...

    def get_task(self, task_id: int) -> StrDict: ...

    def update_task(self, task_id: int, data: StrDict) -> None: ...

    def delete_task(self, task_id: int) -> None: ...

    def list_tasks(self) -> list[StrDict]: ...

    def close(self) -> None: ...

    def open(self) -> None: ...
