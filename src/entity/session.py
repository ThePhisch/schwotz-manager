from datetime import datetime
from pydantic import BaseModel, Field
from typing import Optional


class Session(BaseModel):
    id: Optional[int] = Field(None, gt=0)
    user_id: int
    token: str
    expires_at: Optional[datetime]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    def obfuscate(self) -> "Session":
        return Session(
            id=self.id,
            user_id=self.user_id,
            token="",
            expires_at=self.expires_at,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )
