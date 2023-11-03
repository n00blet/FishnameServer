import asyncio

from fastapi import FastAPI

from src.api.core.config import settings
from src.api.db.base_class import Base
from src.api.db.session import engine
from src.api.routers.fishnames_router import fishnames_router
from src.api.core.service import update_data

app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION, docs_url="/", redoc_url="/docs")


def create_tables():
    Base.metadata.create_all(bind=engine)


async def startup_event():
    # Schedule the data fetching task in the background
    create_tables()
    asyncio.create_task(update_data())


@app.on_event("startup")
async def startup_wrapper():
    await startup_event()


app.include_router(fishnames_router, tags=["FishNames"])
