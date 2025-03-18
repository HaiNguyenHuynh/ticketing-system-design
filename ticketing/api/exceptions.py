from fastapi import HTTPException, status
from application.exceptions import TicketNotFoundError

async def http_error_handler(_, exc):
    """Convert domain exceptions to HTTP exceptions"""
    if isinstance(exc, TicketNotFoundError):
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc)
        )
    # Add other exceptions
    raise exc

def add_exception_handlers(app: FastAPI):
    app.add_exception_handler(TicketNotFoundError, http_error_handler)