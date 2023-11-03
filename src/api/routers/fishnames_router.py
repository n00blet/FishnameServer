from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from src.api.db.repository.fish_repo import retrieve_random_fish_name
from src.api.db.session import get_db
from src.api.schemas.fish import FishName

fishnames_router = APIRouter()


@fishnames_router.get("/random_fish_name", response_model=FishName)
async def get_random_fish_name(db: Session = Depends(get_db)):
    random_fish_name = retrieve_random_fish_name(db=db)
    if random_fish_name:
        return random_fish_name
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No available fish names found",
        )
