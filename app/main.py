from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .models.movie import Base
from .database import engine
from .routers import movies


@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    lifespan=lifespan,
    title="Movies API",
    version="1.0.0",
    summary="API for managing movies",
)

app.include_router(movies.router)