from sqlalchemy import UUID, Column, Enum, String
from sqlalchemy.orm import declarative_base

from domain.enums import PriorityLevel, TicketStatus

Base = declarative_base()


class TicketModel(Base):
    __tablename__ = "tickets"

    id = Column(UUID, primary_key=True)
    title = Column(String(100))
    description = Column(String(1000))
    status = Column(Enum(TicketStatus))
    priority = Column(Enum(PriorityLevel))
    requester_id = Column(UUID)
    assigned_agent_id = Column(UUID, nullable=True)
