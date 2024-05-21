from fastapi import FastAPI
from .core.config import settings
from app.db.session import engine, SessionLocal
from app.db import base, models



base.Base.metadata.create_all(bind=engine)


app = FastAPI(title=settings.PROJECT_NAME)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





@app.get("/")
def test():
    return "test...."