from datetime import timedelta, datetime
import secrets
from src.entity.session import Session
from src.entity.user import User
from src.typing import StrDict
from src.usecase.generic import DBInterface, Usecase
from src.usecase.user import UserDBInterface

class SessionDBInterface(DBInterface):
    def new_session(self, session: StrDict) -> None: ...

    def close_session(self, token: str) -> None: ...

    def get_session(self, token: str) -> dict: ...

class SessionUsecases(Usecase[SessionDBInterface]):
    # special case, since we need two DB Interfaces
    def __init__(self, sessiondb: SessionDBInterface, userdb: UserDBInterface) -> None:
        self.sessiondb = sessiondb
        self.userdb = userdb
        self.expiry = timedelta(days=1)

    def new_session(self, username: str, password: str) -> str:
        user_id = self.userdb.get_id_from_username(username)
        user = User(**self.userdb.get_user(user_id))
        if user.password != password:
            raise ValueError("Invalid password")
        token = secrets.token_hex(16)
        now = datetime.now()
        self.sessiondb.new_session(session=Session(
            id=None,
            user_id=user_id,
            token=token,
            expires_at=now + self.expiry,
            created_at=now,
            updated_at=now
        ).model_dump())
        return token

    def close_session(self, token: str) -> None:
        self.sessiondb.close_session(token)

    def get_session(self, token: str) -> Session:
        try:
            return Session(**self.sessiondb.get_session(token)).obfuscate()
        except Exception as e:
            raise ValueError("Session not found")