from fastapi import APIRouter

router = APIRouter()

@router.get("/live")
async def liveness_check():
    return {"status": "ok"}

@router.get("/ready")
async def readiness_check():
    # Add database/queue checks
    return {"status": "ok"}