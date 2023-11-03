import httpx
import logging

from src.api.core.config import settings
from src.api.db.models.fish import FishDB
from src.api.db.session import SessionLocal, engine

# Initialize logger
logger = logging.getLogger(__name__)

headers = {
    "X-RapidAPI-Key": settings.API_KEY,
    "X-RapidAPI-Host": settings.API_HOST,
}


async def fetch_fishnames_data() -> dict:
    """
    Fetch fish names data from an external API.

    Returns:
        dict: JSON data containing fish names.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url=settings.API_URL, headers=headers)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as http_err:
        logger.error(f"HTTP error occurred: {http_err}")
        return {}
    except Exception as err:
        logger.error(f"An error occurred: {err}")
        return {}


async def update_data():
    """
    Update fish names data in the database if the table is empty.
    """
    # Check if db table is empty
    if FishDB.table_exists(engine=engine):
        logger.info("Database table is not empty. Skipping update.")
        return

    fishnames_data = await fetch_fishnames_data()

    if not fishnames_data:
        logger.warning("Failed to fetch fish names data. Skipping update.")
        return

    db = SessionLocal()
    existing_names = set()

    try:
        for fish_data in fishnames_data:
            name = fish_data.get("name")

            # Check if the name is a duplicate, skip if it is
            if name in existing_names:
                logger.info(f"Ignoring duplicate name: {name}")
                continue

            # Add the name to the set
            existing_names.add(name)

            # Insert the record into the database
            fish = FishDB(id=fish_data.get("id"), name=name)
            db.add(fish)
        db.commit()
        logger.info("Data update completed successfully.")
    except Exception as err:
        db.rollback()
        logger.error(f"Error occurred during data update: {err}")
    finally:
        db.close()

