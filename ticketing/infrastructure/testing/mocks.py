from unittest.mock import Mock

from domain.repositories import TicketRepository


class MockTicketRepository(TicketRepository):
    def __init__(self):
        self.tickets = {}
        self.save = Mock()
        self.find_by_id = Mock()

    async def save(self, ticket):
        self.tickets[ticket.ticket_id] = ticket
        self.save(ticket)

    async def find_by_id(self, ticket_id):
        return self.tickets.get(ticket_id)
