from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from infrastructure.config import settings

class EmailService:
    def __init__(self):
        self.client = SendGridAPIClient(api_key=settings.sendgrid_api_key)

    def send_ticket_notification(self, to_email: str, ticket_id: str):
        message = Mail(
            from_email="support@ticketing.com",
            to_emails=to_email,
            subject="New Ticket Created",
            html_content=f"Your ticket (ID: {ticket_id}) has been created."
        )
        self.client.send(message)