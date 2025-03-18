from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class ContactDetails(BaseModel):
    email: str
    phone: str | None = None

    class Config:
        frozen = True  # Immutable


class Comment(BaseModel):
    comment_id: UUID
    content: str
    author_id: UUID  # ID of the user (agent/customer)
    created_at: datetime = datetime.now()

    class Config:
        frozen = True  # Immutable
