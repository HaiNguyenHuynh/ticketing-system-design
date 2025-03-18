from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

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