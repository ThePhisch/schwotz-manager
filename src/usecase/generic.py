from typing import Protocol


class DBInterface(Protocol):
    def close(self) -> None: ...

    def open(self) -> None: ...

    def create_table(self) -> None: ...

class Usecase[DB: DBInterface]:
    def __init__(self, db: DB) -> None:
        self.db = db