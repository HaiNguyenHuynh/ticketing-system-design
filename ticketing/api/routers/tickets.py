from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, status

from api.dependencies import get_ticket_service
from api.schemas.tickets import (TicketAssignRequest, TicketCreateRequest,
                                 TicketResponse)
from application.services.ticket_service import TicketService

router = APIRouter()


@router.post("/", response_model=TicketResponse, status_code=status.HTTP_201_CREATED)
async def create_ticket(
    request: TicketCreateRequest, service: TicketService = Depends(get_ticket_service)
):
    """Create a new support ticket"""
    return await service.create_ticket(request.to_command())


@router.patch("/{ticket_id}/assign", response_model=TicketResponse)
async def assign_ticket(
    ticket_id: UUID,
    request: TicketAssignRequest,
    service: TicketService = Depends(get_ticket_service),
):
    """Assign ticket to an agent"""
    return await service.assign_ticket(ticket_id, request.to_command())


@router.get("/{ticket_id}", response_model=TicketResponse)
async def get_ticket(
    ticket_id: UUID, service: TicketService = Depends(get_ticket_service)
):
    """Get ticket details"""
    return await service.get_ticket(ticket_id)
