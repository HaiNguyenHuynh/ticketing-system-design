from typing import Optional
from uuid import UUID

from application.dtos.tickets.commands import (AssignTicketCommand,
                                               CreateTicketCommand)
from application.dtos.tickets.responses import TicketResponse
from application.exceptions import (ApplicationException,
                                    InvalidTicketAssignmentError,
                                    TicketNotFoundError)
from domain.entities import Ticket
from domain.events import TicketAssignedEvent, TicketCreatedEvent
from domain.exceptions import DomainException
from domain.repositories import TicketRepository
from ticketing.infrastructure.messaging.event_bus import KafkaEventBus


class TicketService:
    def __init__(self, ticket_repo: TicketRepository, event_bus: KafkaEventBus):
        self.ticket_repo = ticket_repo
        self.event_bus = event_bus

    async def create_ticket(self, command: CreateTicketCommand) -> TicketResponse:
        """Create a new ticket"""
        try:
            ticket = Ticket(
                title=command.title,
                description=command.description,
                priority=command.priority,
                requester_id=command.requester_id,
            )

            await self.ticket_repo.save(ticket)
            self.event_bus.publish(
                TicketCreatedEvent(ticket_id=ticket.ticket_id, title=ticket.title)
            )

            return TicketResponse.from_entity(ticket)

        except DomainException as e:
            raise ApplicationException(str(e)) from e

    async def assign_ticket(
        self, ticket_id: UUID, command: AssignTicketCommand
    ) -> TicketResponse:
        """Assign ticket to an agent"""
        ticket = await self.ticket_repo.find_by_id(ticket_id)
        if not ticket:
            raise TicketNotFoundError()

        try:
            ticket.assign_to_agent(command.agent_id)
            await self.ticket_repo.save(ticket)

            self.event_bus.publish(
                TicketAssignedEvent(
                    ticket_id=ticket.ticket_id, agent_id=command.agent_id
                )
            )

            return TicketResponse.from_entity(ticket)

        except DomainException as e:
            raise InvalidTicketAssignmentError(str(e)) from e

    async def get_ticket(self, ticket_id: UUID) -> TicketResponse:
        """Retrieve a ticket"""
        ticket = await self.ticket_repo.find_by_id(ticket_id)
        if not ticket:
            raise TicketNotFoundError()
        return TicketResponse.from_entity(ticket)
