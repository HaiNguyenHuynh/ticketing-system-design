from confluent_kafka import Producer

from domain.events import TicketAssignedEvent, TicketCreatedEvent
from infrastructure.config import settings


class KafkaEventBus:
    def __init__(self):
        self.producer = Producer(
            {"bootstrap.servers": settings.kafka_bootstrap_servers}
        )

    def publish(self, event):
        if isinstance(event, TicketCreatedEvent):
            self.producer.produce(
                "ticket_created",
                key=str(event.ticket_id),
                value=event.model_dump_json(),
            )
        elif isinstance(event, TicketAssignedEvent):
            self.producer.produce(
                "ticket_assigned",
                key=str(event.ticket_id),
                value=event.model_dump_json(),
            )
