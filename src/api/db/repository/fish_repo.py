from sqlalchemy import func
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from src.api.db.models.fish import FishDB


def retrieve_random_fish_name(db: Session):
    try:
        fishname = db.query(FishDB).filter(FishDB.used.is_(False)).order_by(func.random()).first()
        if fishname:
            fishname.used = True
            db.commit()
            return fishname
        else:
            return None  # Return None when there are no available fish names
    except NoResultFound:
        return None
