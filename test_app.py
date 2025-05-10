import pytest
from app import app, mongo

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_songs(client):
    response = client.get('/songs')
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_search_songs(client):
    response = client.get('/search?message=Lycanthropic')
    assert response.status_code == 200
    assert len(response.json) > 0

