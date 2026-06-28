from fastapi import FastAPI, Depends
from app.api import router
from app.database.session import get_db

app = FastAPI()

app.include_router(router, prefix="/api")

@app.get("/", include_in_schema=True)
def home():
    return {
        "message": "main application is running ✅🚀🚀🚀"
    }

@app.get("/health")
def health(db=Depends(get_db)):
    return {"status": "db connected 🚀🚀✅✅"}