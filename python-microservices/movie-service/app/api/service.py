import requests

url = 'http://172.17.0.1:8080/api/v1/casts/'

def is_cast_present(cast_id: int):
    r = requests.get(f'{url}{cast_id}/')
    return True if r.status_code == 200 else False
