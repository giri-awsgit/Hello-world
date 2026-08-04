from fastapi import FastAPI
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gold Jewellery Billing", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok", "app": "Gold Jewellery Billing System"}
