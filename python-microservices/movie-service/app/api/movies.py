from typing import List
from fastapi import Header, APIRouter, HTTPException

from app.api.models import MovieIn, MovieOut, MovieUpdate
from app.api import db_manager
from app.api.service import is_cast_present

movies = APIRouter()

@movies.post('/', response_model=MovieOut, status_code=201)
async def create_movie(payload: MovieIn):
    for cast_id in payload.casts_id:
        if not is_cast_present(cast_id):
            raise HTTPException(status_code=404, detail=f"Cast with id:{cast_id} not found")

    movie_id = await db_manager.add_movie(payload)
    response = {
        'id': movie_id,
        **payload.dict()
    }

    return response

@movies.get('/', response_model=List[MovieOut])
async def get_movies():
    return await db_manager.get_all_movies()

@movies.get('/movies_with_cast', response_model=List[MovieOut])
async def get_movies_with_cast(cast_id: int):
    movies = await db_manager.get_all_movies_with_cast(cast_id)
    if not movies:
        raise HTTPException(status_code=404, detail="Movies not found")
    return movies

@movies.get('/{id}/', response_model=MovieOut)
async def get_movie(id: int):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

@movies.put('/{id}/')
async def update_movie(id: int, payload: MovieUpdate):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    update_data = payload.dict(exclude_unset=True)

    if 'casts_id' in update_data:
        for cast_id in payload.casts_id:
            if not is_cast_present(cast_id):
                raise HTTPException(status_code=404, detail=f"Cast with given id:{cast_id} not found")

    movie_in_db = MovieIn(**movie)
    print(*movie_in_db)
    updated_movie = movie_in_db.copy(update=update_data)
    print(*updated_movie)
    return await db_manager.update_movie(id, updated_movie)

@movies.delete('/{id}', response_model=None)
async def delete_movie(id: int):
    movie = await db_manager.get_movie(id)
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return await db_manager.delete_movie(id)