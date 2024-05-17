from typing import Protocol

from src.entity.user import User
from src.usecase.generic import DBInterface, Usecase


class UserDBInterface(DBInterface):
    def add_user(self, user: dict) -> int: ...

    def get_user(self, user_id: int) -> dict: ...

    def update_user(self, user_id: int, data: dict) -> None: ...

    def delete_user(self, user_id: int) -> None: ...

    def list_users(self) -> list[dict]: ...

    def get_id_from_username(self, username: str) -> int: ...


class UserUsecases(Usecase[UserDBInterface]):

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

    def get_id_from_username(self, username: str) -> int:
        return self.db.get_id_from_username(username)