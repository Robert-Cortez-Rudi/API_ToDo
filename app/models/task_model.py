from pydantic import Field
from beanie import Document, Indexed, Link, before_event, Replace, Insert
from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime, timezone
from .user_model import User

class Task(Document):
    task_id: UUID = Field(default_factory=uuid4, unique=True)
    status: bool = False
    title: Indexed(str) # type: ignore 
    description: Indexed(str) # type: ignore
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    owner: Link[User]

    def __repr__(self) -> str:
        return f"Task {self.title}"

    def __str__(self) -> str:
        return self.title

    def __hash__(self) -> str:
        return hash(self.title)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Task):
            return self.task_id == other.task_id
        return False
    
    @before_event([Replace, Insert])
    def sync_update_at(self):
        self.updated_at = datetime.now(timezone.utc)
