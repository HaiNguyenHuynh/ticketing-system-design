from fastapi import APIRouter, Depends
from application.dtos.create_ticket import CreateTicketInput, CreateTicketOutput
from application.services.ticket_service import TicketApplicationService
from infrastructure.dependencies import get_ticket_service

router = APIRouter()

@router.post("/tickets", response_model=CreateTicketOutput)
def create_ticket(
    input: CreateTicketInput,
    service: TicketApplicationService = Depends(get_ticket_service)
):
    return service.create_ticket(input)