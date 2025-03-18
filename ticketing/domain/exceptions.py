class DomainException(Exception):
    """Base exception for domain errors"""
    pass

class TicketAssignmentError(DomainException):
    """Raised when ticket assignment fails"""
    pass

class InvalidStatusTransitionError(DomainException):
    """Raised when an invalid status change is attempted"""
    pass