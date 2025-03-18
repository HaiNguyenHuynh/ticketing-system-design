from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from domain.enums import TicketStatus, PriorityLevel

class TicketCreateRequest(BaseModel):
    """Request schema for ticket creation"""
    title: str = Field(..., min_length=1, max_length=100, example="Login failed")
    description: str = Field(..., example="Can't access account")
    priority: PriorityLevel = Field(example="medium")

    def to_command(self):
        from application.dtos.tickets.commands import CreateTicketCommand
        return CreateTicketCommand(**self.model_dump())

class TicketAssignRequest(BaseModel):
    """Request schema for ticket assignment"""
    agent_id: UUID = Field(..., example="a1b2c3d4-...")

    def to_command(self):
        from application.dtos.tickets.commands import AssignTicketCommand
        return AssignTicketCommand(**self.model_dump())

class TicketResponse(BaseModel):
    """Response schema for tickets"""
    ticket_id: UUID
    title: str
    description: str
    status: TicketStatus
    priority: PriorityLevel
    requester_id: UUID
    assigned_agent_id: UUID | None
    created_at: datetime
    updated_at: datetime