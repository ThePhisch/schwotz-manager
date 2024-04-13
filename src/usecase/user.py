from typing import Protocol

from src.entity.user import User


class UserDBInterface(Protocol):
    def add_user(self, user: dict) -> int: ...

    def get_user(self, user_id: int) -> dict: ...

    def update_user(self, user_id: int, data: dict) -> None: ...

    def delete_user(self, user_id: int) -> None: ...

    def list_users(self) -> list[dict]: ...

    def close(self) -> None: ...

    def open(self) -> None: ...

    def create_table(self) -> None: ...


class UserUsecases:
    def __init__(
        self,
        db: UserDBInterface,
    ) -> None:
        self.db = db

    def add_user(self, user: User) -> int:
        return self.db.add_user(user.model_dump())

    def get_user(self, user_id: int) -> User:
        return User(**self.db.get_user(user_id)).obfuscate()

    def update_user(self, user_id: int, data: User) -> None:
        self.db.update_user(user_id, data.model_dump())

    def delete_user(self, user_id: int) -> None:
        self.db.delete_user(user_id)

    def list_users(self) -> list[User]:
        return [User(**t).obfuscate() for t in self.db.list_users()]