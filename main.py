from fastapi import FastAPI
from app.api import router

app = FastAPI()

app.include_router(router, prefix="/api")

@app.get("/", include_in_schema=True)
def home():
    return {
        "message": "main application is running ✅🚀🚀🚀"
    }