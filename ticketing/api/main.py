from fastapi import FastAPI

from .middleware import add_cors_middleware
from .routers import health, tickets, users

app = FastAPI(title="Ticketing System API", version="1.0.0", docs_url="/docs")

# Include routers
app.include_router(tickets.router, prefix="/api/v1/tickets", tags=["tickets"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(health.router, prefix="/health", tags=["monitoring"])

# Add middleware
add_cors_middleware(app)
