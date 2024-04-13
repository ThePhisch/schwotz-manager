from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    id: Optional[int] = Field(None, gt=0)
    username: str
    password: str

    def obfuscate(self) -> "User":
        return User(id=self.id, username=self.username, password="")
