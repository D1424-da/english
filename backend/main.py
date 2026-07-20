from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os
from dotenv import load_dotenv

from app.database import engine, Base
from app.routers import health, users, questions, diagnosis, history

load_dotenv()

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="English Diagnosis API",
    description="英語学習診断アプリ - 弱点を見つけ、何を学べばよいかを示す",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
        "docs": "/docs",
        "endpoints": {
            "health": "/api/health",
            "users": "/api/users",
            "questions": "/api/questions",
            "diagnosis": "/api/diagnosis",
            "history": "/api/history",
        },
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
