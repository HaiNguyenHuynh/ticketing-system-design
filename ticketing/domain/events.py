from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from .enums import TicketStatus

class TicketCreatedEvent(BaseModel):
    ticket_id: UUID
    title: str
    requester_id: UUID
    created_at: datetime = datetime.now()

class TicketAssignedEvent(BaseModel):
    ticket_id: UUID
    agent_id: UUID
    assigned_at: datetime = datetime.now()

class TicketStatusChangedEvent(BaseModel):
    ticket_id: UUID
    old_status: TicketStatus
    new_status: TicketStatus
    updated_at: datetime = datetime.now()

# Freeze all events
for event in [TicketCreatedEvent, TicketAssignedEvent, TicketStatusChangedEvent]:
    event.Config = type("Config", (), {"frozen": True})