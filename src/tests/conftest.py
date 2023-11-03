import random
from unittest.mock import Mock

import pytest
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from src.api.db.models.fish import FishDB


@pytest.fixture
def mock_db_session():
    return Mock(spec=Session)


@pytest.fixture
def fish_data():
    fish_data_list = [
        {"id": 1, "name": "Salmon", "used": False},
        {"id": 2, "name": "Tuna", "used": False},
        {"id": 3, "name": "Swordfish", "used": True},
        # Add more fish data as needed
    ]
    return fish_data_list


@pytest.fixture
def available_fish(mock_db_session, fish_data):
    unused_fish_data = [fish for fish in fish_data if not fish["used"]]
    selected_fish = random.choice(unused_fish_data)
    fish = FishDB(**selected_fish)
    mock_db_session.query.return_value.filter.return_value.order_by.return_value.first.return_value = fish
    return fish


@pytest.fixture
def no_available_fish(mock_db_session):
    mock_db_session.query.return_value.filter.return_value.order_by.return_value.first.side_effect = NoResultFound
    return None


@pytest.fixture
def database_error(mock_db_session):
    mock_db_session.query.return_value.filter.return_value.order_by.return_value.first.side_effect = Exception(
        "Database error")
    return None
