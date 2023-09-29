from fastapi import FastAPI
from database import DATABASE
from core.adapters.User_repository import PostgresUserRepository
# from core.adapters.Movie_repository import MovieRepository

app = FastAPI()
db = DATABASE()
PostgresData = PostgresUserRepository(db)
# MovieData = MovieRepository(db)


@app.get("/")
def root():
    return {"msg": f"{PostgresData.get_users()}"}
