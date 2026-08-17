from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.database import Base, engine, SessionLocal
from app.models.user import User
from app.routers import auth
from app.services.auth_service import hash_password

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

app.mount("/static", StaticFiles(directory="frontend/static"), name="static")


@app.get("/")
def serve_login():
    return FileResponse("frontend/login.html")


@app.get("/app")
def serve_app():
    return FileResponse("frontend/app.html")


@app.get("/health")
def health():
    return {"status": "ok", "app": "Aurum Billing System"}
