import pytest
import requests

@pytest.fixture
def new_movie():
    return {"name": "Test Movie", "plot": "Something tests", "genres": ["Drama", "Horror"], "casts_id": [3]}

@pytest.fixture
def movie_with_incorrect_cast():
    return {"name": "Test Movie", "plot": "Something tests", "genres": ["Drama", "Horror"], "casts_id": [2]}

def test_add_movie_then_delete(new_movie):
    url =  'http://127.0.0.1:8080/api/v1/movies'
    response = requests.post(url, json=new_movie)

    assert response.status_code == 201
    assert response.headers["Content-Type"] == "application/json"

    movie = response.json()
    assert "id" in movie
    assert movie["name"] == "Test Movie"
    assert movie["plot"] == "Something tests"
    assert movie["genres"] == ["Drama", "Horror"]
    assert movie["casts_id"] == [3]

    url = f'http://127.0.0.1:8080/api/v1/movies/{movie["id"]}'
    response = requests.delete(url)

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    assert response.text == 'null'

def test_add_movie_with_incorrect_cast(movie_with_incorrect_cast):
    url =  'http://127.0.0.1:8080/api/v1/movies'
    response = requests.post(url, json=movie_with_incorrect_cast)

    assert response.status_code == 404
    assert response.headers["Content-Type"] == "application/json"
