class ApplicationException(Exception):
    """Base exception for application layer errors"""
    detail: str = "Application error"

class TicketNotFoundError(ApplicationException):
    detail: str = "Ticket not found"

class InvalidTicketAssignmentError(ApplicationException):
    detail: str = "Invalid ticket assignment"

class NotificationFailedError(ApplicationException):
    detail: str = "Notification failed"