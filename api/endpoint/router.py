from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from core.adapters.Movie_repository import PostgresMovieRepository
from database import DATABASE
import base64
from typing import List
import json
router = APIRouter()
db = DATABASE()
MovieData = PostgresMovieRepository(db)


@router.get("/movies")
def get_movies():
    return {"data": MovieData.get_movies()}


@router.get("/movie/{movie_id}")
def get_movie(movie_id: int):
    movie = MovieData.get_movie(movie_id)
    if movie:
        return {"data": movie}
    else:
        raise HTTPException(status_code=404, detail="Movie not found")


@router.post("/create_movie")
async def create_movie(
    file: UploadFile = File(...),
    movie_data: UploadFile = File(...),

):
    try:
        # อ่านข้อมูล JSON จากไฟล์
        movie_data_content = await movie_data.read()
        movie_data_dict = json.loads(movie_data_content)

        # ต่อไปดำเนินการเหมือนเดิม
        m_id = movie_data_dict.get("m_id")
        m_name = movie_data_dict.get("m_name")
        duration = movie_data_dict.get("duration")
        rating = movie_data_dict.get("rating")
        story = movie_data_dict.get("story")
        c_id = movie_data_dict.get("c_id")
        with open(file.filename, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode("utf-8")
        data = {
            "m_id": m_id,
            "m_name": m_name,
            "duration": duration,
            "rating": rating,
            "story": story,
            "image": base64_image,
            "c_id": c_id
        }
        MovieData.create_movie(data)
    except FileNotFoundError:
        raise HTTPException(status_code=400, detail="File not found")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Internal server error: {str(e)}")

    return {"msg": "Create Suscess"}
