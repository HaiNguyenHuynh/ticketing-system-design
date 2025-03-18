from fastapi import Depends
from dependency_injector.wiring import Provide, inject
from infrastructure.persistence.database import get_db
from application.container import ApplicationContainer

def get_ticket_service(
    db: AsyncSession = Depends(get_db)
) -> TicketService:
    """Dependency for ticket service"""
    return ApplicationContainer.ticket_service(db=db)

# For authentication (example)
async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    user = authenticate_user(token)
    return user