from fastapi import FastAPI

from app.routes import ai


app = FastAPI(
    title="Aletheia Investigation Workbench",
    description="MVP backend for structured fraud investigation support.",
    version="0.1.0",
)


app.include_router(ai.router)


@app.get("/")
def read_root():
    return {
        "message": "Fraud Investigation Workbench API is running"
    }
