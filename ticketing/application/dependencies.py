from dependency_injector import containers, providers
from infrastructure.persistence.repositories import SqlAlchemyTicketRepository
from infrastructure.messaging.event_bus import KafkaEventBus
from infrastructure.persistence.database import async_session_factory

class ApplicationContainer(containers.DeclarativeContainer):
    # Infrastructure components
    db_session = providers.Singleton(async_session_factory)
    event_bus = providers.Singleton(KafkaEventBus)
    
    # Repositories
    ticket_repo = providers.Factory(
        SqlAlchemyTicketRepository,
        session=db_session
    )
    
    # Services
    ticket_service = providers.Factory(
        "application.services.ticket_service.TicketService",
        ticket_repo=ticket_repo,
        event_bus=event_bus
    )