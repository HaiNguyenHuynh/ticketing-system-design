from uuid import UUID
from domain.entities import Ticket
from domain.repositories import TicketRepository
from domain.events import TicketCreatedEvent
from domain.exceptions import DomainException
from application.dtos.create_ticket import CreateTicketInput, CreateTicketOutput

class TicketApplicationService:
    def __init__(
        self,
        ticket_repo: TicketRepository,
        event_bus: EventBus  # Defined in infrastructure
    ):
        self.ticket_repo = ticket_repo
        self.event_bus = event_bus

    def create_ticket(self, input: CreateTicketInput) -> CreateTicketOutput:
        # Validate business rules
        ticket = Ticket(
            title=input.title,
            description=input.description,
            priority=input.priority,
            requester_id=UUID(input.requester_id)
        )

        # Persist the ticket
        self.ticket_repo.save(ticket)

        # Publish domain event
        self.event_bus.publish(TicketCreatedEvent(
            ticket_id=ticket.ticket_id,
            title=ticket.title
        ))

        return CreateTicketOutput(
            ticket_id=str(ticket.ticket_id),
            status=ticket.status.value
        )