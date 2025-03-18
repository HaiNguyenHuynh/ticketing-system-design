from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from domain.enums import TicketStatus, PriorityLevel

class TicketResponse(BaseModel):
    ticket_id: UUID
    title: str
    description: str
    status: TicketStatus
    priority: PriorityLevel
    requester_id: UUID
    assigned_agent_id: Optional[UUID]
    created_at: datetime
    updated_at: datetime

    @classmethod
    def from_entity(cls, ticket: Ticket) -> "TicketResponse":
        return cls(
            ticket_id=ticket.ticket_id,
            title=ticket.title,
            description=ticket.description,
            status=ticket.status,
            priority=ticket.priority,
            requester_id=ticket.requester_id,
            assigned_agent_id=ticket.assigned_agent_id,
            created_at=ticket.created_at,
            updated_at=ticket.updated_at
        )

class TicketListResponse(BaseModel):
    tickets: list[TicketResponse]
    total: int
    page: int
    page_size: int