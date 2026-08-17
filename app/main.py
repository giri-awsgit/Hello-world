import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.database import Base, engine, SessionLocal
from app.models.user import User
from app.routers import auth
from app.services.auth_service import hash_password

# KC_BASE_DIR is set by run_app.py when packaged (points to sys._MEIPASS).
# In dev it falls back to the project root (one level up from app/).
_base = os.getenv("KC_BASE_DIR") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
FRONTEND_DIR = os.path.join(_base, "frontend")
STATIC_DIR   = os.path.join(FRONTEND_DIR, "static")

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Krishna Chains Billing", version="0.1.0")


def seed_admin():
    db = SessionLocal()
    try:
        if not db.query(User).first():
            admin = User(username="rkc", password_hash=hash_password("rkc0345"))
            db.add(admin)
            db.commit()
    finally:
        db.close()


seed_admin()

app.include_router(auth.router)

app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/")
def serve_login():
    return FileResponse(os.path.join(FRONTEND_DIR, "login.html"))


@app.get("/app")
def serve_app():
    return FileResponse(os.path.join(FRONTEND_DIR, "app.html"))


@app.get("/health")
def health():
    return {"status": "ok", "app": "Krishna Chains Billing"}
