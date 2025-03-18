from uuid import UUID
from .entities import Ticket
from .repositories import TicketRepository, UserRepository
from .exceptions import TicketAssignmentError

class TicketAssignmentService:
    """Domain service for assigning tickets to agents"""
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def assign_ticket(self, ticket: Ticket, agent_id: UUID) -> None:
        agent = self.user_repo.find_by_id(agent_id)
        if not agent or agent.role != "agent":
            raise TicketAssignmentError("Invalid agent ID")
        ticket.assign_to_agent(agent_id)

class SlaMonitoringService:
    """Checks SLA compliance for tickets"""
    def check_sla_violation(self, ticket: Ticket) -> bool:
        # Example: High-priority tickets must be resolved in 24 hours
        if ticket.priority == "high" and (datetime.now() - ticket.created_at).days > 1:
            return True
        return False