from fastapi import APIRouter
from sqlalchemy import text

from ..database import engine

router = APIRouter()


@router.get("/health")
async def health_check():
    db_status = "ok"
    db_error = None
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
    except Exception as e:
        db_status = "error"
        db_error = str(e).split("\n")[0][:200]

    return {
        "status": "ok" if db_status == "ok" else "degraded",
        "message": "English Diagnosis API is running",
        "database": db_status,
        **({"database_error": db_error} if db_error else {}),
    }
