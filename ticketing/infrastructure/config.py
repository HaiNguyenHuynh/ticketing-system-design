from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database
    database_url: str = "postgresql+asyncpg://user:pass@localhost/ticketing"
    
    # Messaging
    kafka_bootstrap_servers: str = "localhost:9092"
    
    # Email
    sendgrid_api_key: str = ""
    
    # SMS
    twilio_account_sid: str = ""
    twilio_auth_token: str = ""
    
    class Config:
        env_file = ".env"

settings = Settings()