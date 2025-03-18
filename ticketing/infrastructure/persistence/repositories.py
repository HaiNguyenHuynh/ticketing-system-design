from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from domain.entities import Ticket
from domain.repositories import TicketRepository

class SqlAlchemyTicketRepository(TicketRepository):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, ticket: Ticket):
        from .models import TicketModel  # Local import to avoid circular dependency
        
        ticket_model = TicketModel(
            id=ticket.ticket_id,
            title=ticket.title,
            description=ticket.description,
            status=ticket.status,
            priority=ticket.priority,
            requester_id=ticket.requester_id,
            assigned_agent_id=ticket.assigned_agent_id
        )
        self.session.add(ticket_model)
        await self.session.commit()

    async def find_by_id(self, ticket_id: UUID) -> Ticket | None:
        from .models import TicketModel
        
        result = await self.session.execute(
            select(TicketModel).where(TicketModel.id == ticket_id)
        )
        ticket_model = result.scalar_one_or_none()
        
        if not ticket_model:
            return None
            
        return Ticket(
            ticket_id=ticket_model.id,
            title=ticket_model.title,
            description=ticket_model.description,
            status=ticket_model.status,
            priority=ticket_model.priority,
            requester_id=ticket_model.requester_id,
            assigned_agent_id=ticket_model.assigned_agent_id
        )