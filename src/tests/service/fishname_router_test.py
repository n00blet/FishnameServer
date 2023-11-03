from unittest.mock import patch

from fastapi.testclient import TestClient

from src.api.main import app

client = TestClient(app)


@patch("src.api.routers.fishnames_router.retrieve_random_fish_name")
def test_get_random_fish_name_with_available_fish(mock_retrieve_fish, mock_db_session):
    # Mocking the retrieve_random_fish_name function to return a fish
    mock_fish = {"id": 1, "name": "Salmon", "used": False}
    mock_retrieve_fish.return_value = mock_fish

    response = client.get("/random_fish_name")
    assert response.status_code == 200
    assert response.json()['name'] == "Salmon"


@patch("src.api.routers.fishnames_router.retrieve_random_fish_name")
def test_get_random_fish_name_with_no_available_fish(mock_retrieve_fish, mock_db_session):
    # Mocking the retrieve_random_fish_name function to return None
    mock_fish = None
    mock_retrieve_fish.return_value = mock_fish

    response = client.get("/random_fish_name")

    assert response.status_code == 404
    assert response.json() == {"detail": "No available fish names found"}
