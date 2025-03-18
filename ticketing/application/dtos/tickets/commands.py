from uuid import UUID

from pydantic import BaseModel, Field

from domain.enums import PriorityLevel


class CreateTicketCommand(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: str
    priority: PriorityLevel
    requester_id: UUID


class AssignTicketCommand(BaseModel):
    agent_id: UUID


class AddCommentCommand(BaseModel):
    content: str = Field(..., min_length=1, max_length=500)
    author_id: UUID
