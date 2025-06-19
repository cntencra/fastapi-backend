from fastapi import FastAPI
from contextlib import asynccontextmanager

from fastapi_backend.db import db_manager
from fastapi_backend.app.routes import api

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await db_manager.open_pool()
    yield
    # Shutdown
    await db_manager.close_pool()


app = FastAPI()

app.include_router(api.router, prefix="/api")