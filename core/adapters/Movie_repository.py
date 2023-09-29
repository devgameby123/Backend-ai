from typing import List, Optional
from core.ports.Movie_repository import MovieRepository


class PostgresMovieRepository(MovieRepository):
    def __init__(self, db):
        self.DB = db

    def create_movie(self, movie_data: dict) -> dict:
        pass

    def get_movie(self, movie_id: int) -> Optional[dict]:
        pass

    def get_movies(self) -> dict:
        select_query = "SELECT * FROM movie"
        result = self.DB.execute_select_query(select_query)
        movies_dict = {movie[0]: movie[1] for movie in result}
        return movies_dict
