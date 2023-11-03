from src.api.db.repository.fish_repo import retrieve_random_fish_name


def test_retrieve_random_fish_name_with_available_fish(available_fish, mock_db_session):
    retrieved_fish_name = retrieve_random_fish_name(mock_db_session)
    assert retrieved_fish_name == available_fish
    assert retrieved_fish_name.used is True


def test_retrieve_random_fish_name_with_no_available_fish(no_available_fish, mock_db_session):
    retrieved_fish_name = retrieve_random_fish_name(mock_db_session)
    assert retrieved_fish_name is None


def test_retrieve_random_fish_name_with_database_error(database_error, mock_db_session):
    mock_db_session.query().filter().order_by().first.side_effect = Exception("Database error")

    try:
        retrieved_fish_name = retrieve_random_fish_name(mock_db_session)
        print(retrieved_fish_name)
        assert retrieved_fish_name is None
    except Exception as e:
        # Handle the exception or assert specific behavior if necessary
        assert str(e) == "Database error"


