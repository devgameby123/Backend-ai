import psycopg2
from typing import List, Optional
from core.ports.Movie_repository import MovieRepository
import base64


class PostgresMovieRepository(MovieRepository):
    def __init__(self, db):
        self.DB = db

    def create_movie(self, movie_data: dict) -> dict:
        pass

    def get_movie(self, movie_id: int) -> Optional[dict]:
        pass

    def get_movies(self) -> dict:
        select_query = "SELECT id, moviename, category, image FROM movies;"
        result = self.DB.execute_select_query(select_query)

        movies_with_images = []

        for movie in result:
            movie_id, moviename, category, image_data = movie
            image_base64 = base64.b64encode(image_data).decode('utf-8')
            movies_with_images.append(
                {"id": movie_id, "moviename": moviename, "category": category, "image": image_base64})

        return movies_with_images
