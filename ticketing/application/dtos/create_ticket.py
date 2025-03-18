from pydantic import BaseModel

class CreateTicketInput(BaseModel):
    title: str
    description: str
    priority: str  # "low", "medium", "high"
    requester_id: str

class CreateTicketOutput(BaseModel):
    ticket_id: str
    status: str