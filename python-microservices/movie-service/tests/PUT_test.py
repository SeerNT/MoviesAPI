import pytest
import requests

@pytest.fixture
def movie_data():
    return {"title": "The Hitchhiker's Guide to the Galaxy", "author": "Douglas Adams"}

def test_update_movie(movie_data):
    url =  'http://127.0.0.1:8080/api/v1/movies/3/'
    response = requests.put(url, json=movie_data)

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
