from fastapi import FastAPI
from database import DATABASE
from core.adapters.User_repository import PostgresUserRepository
from core.adapters.Movie_repository import PostgresMovieRepository

app = FastAPI()
db = DATABASE()

PostgresData = PostgresUserRepository(db)
MovieData = PostgresMovieRepository(db)

"""_summary_
@app.get("/")
def root():
    return {"msg": f"{PostgresData.get_users()}"}
"""


@app.get("/")
def root():
    return {"msg": f"{PostgresData.get_users()}"}


@app.get("/movie")
def root():
    return {"data": MovieData.get_movies()}
