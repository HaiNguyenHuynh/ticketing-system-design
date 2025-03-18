from dependency_injector import containers, providers

from application.services.ticket_service import TicketApplicationService
from infrastructure.messaging.event_bus import KafkaEventBus
from infrastructure.persistence.repositories import SqlAlchemyTicketRepository


class Container(containers.DeclarativeContainer):
    # Infrastructure
    db_session = providers.Singleton(...)  # Initialize SQLAlchemy session
    event_bus = providers.Singleton(KafkaEventBus, bootstrap_servers="localhost:9092")

    # Repositories
    ticket_repo = providers.Factory(SqlAlchemyTicketRepository, db_session=db_session)

    # Application services
    ticket_service = providers.Factory(
        TicketApplicationService, ticket_repo=ticket_repo, event_bus=event_bus
    )


def get_ticket_service() -> TicketApplicationService:
    return Container.ticket_service()
