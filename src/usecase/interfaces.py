"""
Defines the base interfaces for the usecase layer.

The adapters (e.g. in web, db) will implement these interfaces.
"""

from typing import Generator, Protocol


class DBInterface(Protocol):

    def close(self) -> None: ...

    def open(self) -> None: ...

    def create_table(self) -> None: ...
