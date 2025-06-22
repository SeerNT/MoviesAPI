import requests

def test_get_movies():
    url =  'http://127.0.0.1:8080/api/v1/movies'
    response = requests.get(url)

    assert response.status_code == 200

    assert response.headers["Content-Type"] == "application/json"

    movies = response.json()

    for movie in movies:
        assert "name" in movie
        assert "plot" in movie
        assert "genres" in movie
        assert "casts_id" in movie
        assert "id" in movie

def test_get_movies_with_cast():
    url =  'http://127.0.0.1:8080/api/v1/movies/movies_with_cast?cast_id=3'
    response = requests.get(url)

    assert response.status_code == 200

    assert response.headers["Content-Type"] == "application/json"

    movies = response.json()

    for movie in movies:
        assert "name" in movie
        assert "plot" in movie
        assert "genres" in movie
        assert "casts_id" in movie
        assert "id" in movie
        assert 3 in movie["casts_id"]

def test_get_movie_by_id():
    url =  'http://127.0.0.1:8080/api/v1/movies/1/'
    response = requests.get(url)

    assert response.status_code == 200

    assert response.headers["Content-Type"] == "application/json"

    movie = response.json()

    assert "name" in movie
    assert "plot" in movie
    assert "genres" in movie
    assert "casts_id" in movie
    assert "id" in movie
    assert movie["id"] == 1