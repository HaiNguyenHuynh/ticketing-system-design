from abc import ABC, abstractmethod
from uuid import UUID
from .entities import Ticket, User

# Repository interfaces (implemented in infrastructure layer)
class TicketRepository(ABC):
    @abstractmethod
    def save(self, ticket: Ticket) -> None:
        pass

    @abstractmethod
    def find_by_id(self, ticket_id: UUID) -> Ticket | None:
        pass

class UserRepository(ABC):
    @abstractmethod
    def find_by_id(self, user_id: UUID) -> User | None:
        pass