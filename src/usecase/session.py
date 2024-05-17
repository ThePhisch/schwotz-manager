from datetime import timedelta
import secrets
from src.entity.session import Session
from src.entity.user import User
from src.usecase.generic import DBInterface, Usecase
from src.usecase.user import UserDBInterface

class SessionDBInterface(DBInterface):
    def new_session(self, session: Session) -> None: ...

    def close_session(self, token: str) -> None: ...

    def get_session(self, token: str) -> Session: ...

class SessionUsecases:
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
        return token

    def close_session(self, token: str) -> None:
        self.sessiondb.close_session(token)

    def get_session(self, token: str) -> Session:
        raise NotImplementedError