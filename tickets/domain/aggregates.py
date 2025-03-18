from pydantic import BaseModel
from .entities import Ticket
from .value_objects import Comment

class TicketAggregate(BaseModel):
    """Aggregate root for a Ticket and its Comments"""
    ticket: Ticket
    comments: list[Comment] = []

    def add_comment(self, comment: Comment):
        if comment.author_id not in {self.ticket.requester_id, self.ticket.assigned_agent_id}:
            raise ValueError("Unauthorized to comment")
        self.comments.append(comment)
        self.ticket.comments = self.comments  # Sync with Ticket entity