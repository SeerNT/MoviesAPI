import requests

url = 'http://172.17.0.1:8080/api/v1/movies/movies_with_cast?'

def is_movie_with_cast_exists(cast_id: int):
    r = requests.get(f'{url}cast_id={cast_id}')
    return True if r.status_code == 200 else False
