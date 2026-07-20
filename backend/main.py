from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os
import logging
from dotenv import load_dotenv

from sqlalchemy import inspect, text

from app.database import engine, Base
from app.routers import health, users, questions, diagnosis, history

load_dotenv()

DEBUG = os.getenv("DEBUG", "false").lower() == "true"

logging.basicConfig(
    level=logging.DEBUG if DEBUG else logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

Base.metadata.create_all(bind=engine)

inspector = inspect(engine)
if "users" in inspector.get_table_names():
    columns = [col["name"] for col in inspector.get_columns("users")]
    if "password_hash" not in columns:
        try:
            with engine.begin() as conn:
                conn.execute(text("ALTER TABLE users ADD COLUMN password_hash VARCHAR(255)"))
            logger.info("Added password_hash column to users table")
        except Exception:
            logger.debug("password_hash column already added by another worker")

app = FastAPI(
    title="English Diagnosis API",
    description="英語学習診断アプリ - 弱点を見つけ、何を学べばよいかを示す",
    version="0.1.0",
    docs_url="/docs" if DEBUG else None,
    redoc_url="/redoc" if DEBUG else None,
)

allowed_origins = os.getenv("ALLOWED_ORIGINS", "")
if allowed_origins:
    origins = [o.strip() for o in allowed_origins.split(",")]
elif DEBUG:
    origins = ["http://localhost:3000", "http://localhost:5173", "http://localhost:8000"]
else:
    origins = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}", exc_info=True)
    return JSONResponse(status_code=500, content={"detail": "Internal server error"})


app.include_router(health.router, prefix="/api")
app.include_router(users.router, prefix="/api")
app.include_router(questions.router, prefix="/api")
app.include_router(diagnosis.router, prefix="/api")
app.include_router(history.router, prefix="/api")

frontend_dist = os.path.join(os.path.dirname(__file__), "..", "frontend", "dist")
frontend_public = os.path.join(os.path.dirname(__file__), "..", "frontend", "public")
frontend_dir = frontend_dist if os.path.exists(frontend_dist) else frontend_public
if os.path.exists(frontend_dir):
    app.mount("/", StaticFiles(directory=frontend_dir, html=True), name="frontend")


@app.get("/api")
async def api_root():
    return {
        "message": "English Diagnosis API",
        "version": "0.1.0",
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
