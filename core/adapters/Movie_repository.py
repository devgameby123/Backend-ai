import psycopg2
from typing import List, Optional
from core.ports.Movie_repository import MovieRepository
import base64


class PostgresMovieRepository(MovieRepository):
    def __init__(self, db):
        self.DB = db

    def create_movie(self, movie_data: dict):
        try:
            m_id = movie_data.get("m_id")
            m_name = movie_data.get("m_name")
            duration = movie_data.get("duration")
            rating = movie_data.get("rating")
            story = movie_data.get("story")
            image_data = movie_data.get("image")

            c_id = movie_data.get("c_id")
            # สร้างคำสั่ง SQL เพื่อเพิ่มข้อมูล
            insert_query = f"INSERT INTO Movie (m_id,m_name, duration, rating, story, Image) VALUES ({m_id}, '{m_name}', {duration},{rating},'{story}','{image_data}');"
            # ทำการ execute คำสั่ง SQL
            self.DB.execute_insert_query(insert_query)

            for numCategory in c_id:
                # สร้างคำสั่ง SQL เพื่อเพิ่มข้อมูล
                insert_query = f"INSERT INTO Movie_Category (m_id, c_id) VALUES ({m_id},{numCategory});"
                # ทำการ execute คำสั่ง SQL
                self.DB.execute_insert_query(insert_query)

        except Exception as e:
            # ให้ทำการรับรองการผิดพลาดและประมวลผลข้อผิดพลาดต่อไป
            print(f"Error creating movie: {e}")

    def get_movie(self, movie_id: int) -> Optional[dict]:
        try:
            # สร้างคำสั่ง SQL เพื่อดึงข้อมูลของหนังที่มี id ตรงกับ movie_id
            select_query = f'SELECT id, moviename, category, image FROM movies WHERE id = {movie_id};'
            # ทำการ execute คำสั่ง SQL
            result = self.DB.execute_select_query(select_query)

            # ตรวจสอบว่ามีข้อมูลหนังที่ตรงกับ id นี้หรือไม่
            if result:
                movie_id, moviename, category, image_data = result[0]
                image_base64 = base64.b64encode(image_data).decode('utf-8')
                return {"id": movie_id, "moviename": moviename, "category": category, "image": image_base64}
            else:
                return None

        except Exception as e:
            # ให้ทำการรับรองการผิดพลาดและประมวลผลข้อผิดพลาดต่อไป
            print(f"Error getting movie: {e}")
            return None

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
