from datetime import datetime, timedelta


class Task:
    def __init__(
        self, name: str, nextup: datetime, frequency: timedelta, assigned: str
    ) -> None:
        self.id = None
        self.name = name
        self.frequency = frequency
        self.nextup = nextup
        self.assigned = assigned

    def __str__(self) -> str:
        return f"Task: {self.name} - Next up: {self.nextup} - Frequency: {self.frequency} - Assigned: {self.assigned}"

    def __repr__(self) -> str:
        return f"<Task {self.id:>5} name {self.name[:8]}>"

    def assign_id(self, id: int) -> None:
        self.id = id

    def complete(self) -> None:
        self.nextup += self.frequency


def test_list(): ...
