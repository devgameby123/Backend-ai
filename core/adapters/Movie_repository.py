import psycopg2
from typing import List, Optional
from core.ports.Movie_repository import MovieRepository
import base64


class PostgresMovieRepository(MovieRepository):
    def __init__(self, db):
        self.DB = db

    def get_moviebyRating(self) -> dict | None:
        select_query = f"SELECT * FROM Movie ORDER BY rating DESC Limit 4;"
        result = self.DB.execute_select_query(select_query)

        movies_with_images = []

        for movie in result:
            m_id, m_name, duration, rating, story, Image = movie
            if Image is not None:
                image_base64 = base64.b64encode(Image).decode('utf-8')
            else:
                image_base64 = None

            select_query = f"SELECT c_id FROM Movie_Category WHERE m_id ={m_id};"
            category_ids = self.DB.execute_select_query(select_query)
            categories = [category[0] for category in category_ids]
            Alltag = []
            for data in categories:
                select_query = f"SELECT c_name FROM Category WHERE c_id = {data};"
                Tag: str = self.DB.execute_select_query(select_query)
                Alltag.append(Tag)
            tags = [tag[0][0] for tag in Alltag]
            movies_with_images.append({
                "id": m_id,
                "m_name": m_name,
                "duration": duration,
                "rating": rating,
                "story": story,
                "Tag": tags,
                "Image": image_base64
            })

        return movies_with_images

    def get_moviebyCategory(self, c_name: str) -> dict | None:
        select_query = f"SELECT Movie.m_id,Movie.m_name,Movie.duration,Movie.rating,Movie.story,Movie.Image FROM Movie JOIN Movie_Category ON Movie.m_id = Movie_Category.m_id JOIN Category ON Movie_Category.c_id = Category.c_id WHERE Category.c_name = '{c_name}' LIMIT 4;"
        result = self.DB.execute_select_query(select_query)

        movies_with_images = []

        for movie in result:
            m_id, m_name, duration, rating, story, Image = movie
            if Image is not None:
                image_base64 = base64.b64encode(Image).decode('utf-8')
            else:
                image_base64 = None

            select_query = f"SELECT c_id FROM Movie_Category WHERE m_id ={m_id};"
            category_ids = self.DB.execute_select_query(select_query)
            categories = [category[0] for category in category_ids]
            Alltag = []
            for data in categories:
                select_query = f"SELECT c_name FROM Category WHERE c_id = {data};"
                Tag: str = self.DB.execute_select_query(select_query)
                Alltag.append(Tag)
            tags = [tag[0][0] for tag in Alltag]
            movies_with_images.append({
                "id": m_id,
                "m_name": m_name,
                "duration": duration,
                "rating": rating,
                "story": story,
                "Tag": tags,
                "Image": image_base64
            })

        return movies_with_images

    def create_movie(self, movie_data: dict):
        m_id = movie_data.get("m_id")
        m_name = movie_data.get("m_name")
        duration = movie_data.get("duration")
        rating = movie_data.get("rating")
        story = movie_data.get("story")
        image_data = movie_data.get("image")

        c_id = movie_data.get("c_id")
        Comment = movie_data.get("Comment")
        try:

            # สร้างคำสั่ง SQL เพื่อเพิ่มข้อมูล
            insert_query = f"INSERT INTO Movie (m_id,m_name, duration, rating, story, Image) VALUES ({m_id}, '{m_name}', {duration},{rating},'{story}','{image_data}');"
            # ทำการ execute คำสั่ง SQL
            self.DB.execute_insert_query(insert_query)

            for numCategory in c_id:
                # สร้างคำสั่ง SQL เพื่อเพิ่มข้อมูล
                insert_query = f"INSERT INTO Movie_Category (m_id, c_id) VALUES ({m_id},{numCategory});"
                # ทำการ execute คำสั่ง SQL
                self.DB.execute_insert_query(insert_query)

            for numComment in Comment:
                # สร้างคำสั่ง SQL เพื่อเพิ่มข้อมูล
                insert_query = f"INSERT INTO Comment(cmt_text, m_id, create_at) VALUES('{numComment}', {m_id}, CURRENT_TIMESTAMP );"
                self.DB.execute_insert_query(insert_query)
        except Exception as e:
            # ให้ทำการรับรองการผิดพลาดและประมวลผลข้อผิดพลาดต่อไป
            print(f"Error creating movie: {e}")

    def get_movie(self, movie_id: int) -> Optional[dict]:
        select_query = f"SELECT * FROM Movie WHERE m_id = {movie_id};"
        result = self.DB.execute_select_query(select_query)

        movies_with_images = []

        for movie in result:
            m_id, m_name, duration, rating, story, Image = movie
            if Image is not None:
                image_base64 = base64.b64encode(Image).decode('utf-8')
            else:
                image_base64 = None

            select_query = f"SELECT c_id FROM Movie_Category WHERE m_id ={m_id};"
            category_ids = self.DB.execute_select_query(select_query)
            categories = [category[0] for category in category_ids]
            Alltag = []
            for data in categories:
                select_query = f"SELECT c_name FROM Category WHERE c_id = {data};"
                Tag: str = self.DB.execute_select_query(select_query)
                Alltag.append(Tag)
            tags = [tag[0][0] for tag in Alltag]
            movies_with_images.append({
                "id": m_id,
                "m_name": m_name,
                "duration": duration,
                "rating": rating,
                "story": story,
                "Tag": tags,
                "Image": image_base64
            })

        return movies_with_images

    def get_movies(self):
        select_query = "SELECT * FROM Movie;"
        result = self.DB.execute_select_query(select_query)

        movies_with_images = []

        for movie in result:
            m_id, m_name, duration, rating, story, Image = movie
            if Image is not None:
                image_base64 = base64.b64encode(Image).decode('utf-8')
            else:
                image_base64 = None

            select_query = f"SELECT c_id FROM Movie_Category WHERE m_id ={m_id};"
            category_ids = self.DB.execute_select_query(select_query)
            categories = [category[0] for category in category_ids]
            Alltag = []
            for data in categories:
                select_query = f"SELECT c_name FROM Category WHERE c_id = {data};"
                Tag: str = self.DB.execute_select_query(select_query)
                Alltag.append(Tag)
            tags = [tag[0][0] for tag in Alltag]
            movies_with_images.append({
                "id": m_id,
                "m_name": m_name,
                "duration": duration,
                "rating": rating,
                "story": story,
                "Tag": tags,
                "Image": image_base64
            })

        return movies_with_images
    
    def get_movies_search(self, m_name: str) -> list:
        limit = 4
        select_query = f"SELECT Movie.m_id FROM Movie WHERE Movie.m_name LIKE '%{m_name}%' LIMIT {limit};"
        result = self.DB.execute_select_query(select_query)
        
