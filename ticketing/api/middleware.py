from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware


def add_cors_middleware(app: FastAPI):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


async def log_requests(request: Request, call_next):
    """Example custom middleware"""
    print(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    return response
