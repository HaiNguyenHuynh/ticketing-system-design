from datetime import datetime
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, field_validator

from .enums import PriorityLevel, TicketStatus, UserRole
from .value_objects import Comment, ContactDetails


class User(BaseModel):
    user_id: UUID = Field(default_factory=uuid4)
    name: str = Field(..., min_length=1)
    contact: ContactDetails
    role: UserRole = UserRole.CUSTOMER

    @field_validator("name")
    def name_must_contain_space(cls, v):
        if " " not in v:
            raise ValueError("Name must contain a space")
        return v


class Ticket(BaseModel):
    ticket_id: UUID = Field(default_factory=uuid4)
    title: str = Field(..., min_length=1, max_length=100)
    description: str
    status: TicketStatus = TicketStatus.OPEN
    priority: PriorityLevel = PriorityLevel.MEDIUM
    requester_id: UUID  # ID of the User who created the ticket
    assigned_agent_id: UUID | None = None
    comments: list[Comment] = []
    created_at: datetime = Field(default_factory=datetime.now)

    def assign_to_agent(self, agent_id: UUID):
        if self.assigned_agent_id == agent_id:
            raise ValueError("Agent already assigned")
        self.assigned_agent_id = agent_id
        self.status = TicketStatus.IN_PROGRESS

    def change_status(self, new_status: TicketStatus):
        if self.status == new_status:
            raise ValueError("Status is already set to {new_status}")
        self.status = new_status
