from datetime import datetime, timedelta
from pydantic import BaseModel, Field
from typing import Optional

class Task(BaseModel):
    id: Optional[int] = Field(None, gt=0)
    name: str
    timedelta: timedelta
    nextup: datetime
    assigned: Optional[str] = None