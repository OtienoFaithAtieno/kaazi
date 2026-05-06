from fastapi import FastAPI
from backend.api.routes import router

app = FastAPI(title="kaazi")

app.include_router(router)