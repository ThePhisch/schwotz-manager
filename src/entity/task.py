from datetime import datetime, timedelta

from src.typing import StrDict


class Task:
    timeformat = "%Y-%m-%d %H:%M:%S"

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

    def to_dict(self) -> StrDict:
        return {
            "id": self.id,
            "name": self.name,
            "nextup": self.nextup.strftime(Task.timeformat),  # Convert datetime to string
            "frequency": self.frequency.total_seconds(),  # Convert timedelta to string
            "assigned": self.assigned,
        }
