import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()


class DATABASE:
    def __init__(self):
        self.connection = None

    def db_connection(self):
        try:
            self.connection = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD")
            )
            print("\033[92mINFO:\033[0m     Connection established successfully!")
        except psycopg2.Error as e:
            print("Error: Unable to connect to the database:")

    def execute_select_query(self, query):
        try:
            if not self.connection:
                self.db_connection()

            cursor = self.connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()  # หรือ fetchone() ถ้าคุณต้องการข้อมูลเพียงรายการเดียว
            cursor.close()
            return result
        except psycopg2.Error as e:
            print("Error executing SELECT query:", e)
            return []

    def execute_insert_query(self, query, params=None):
        try:
            if not self.connection:
                self.db_connection()

            cursor = self.connection.cursor()

            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            self.connection.commit()
            cursor.close()
            print("\033[92mINFO:\033[0m     INSERT query executed successfully!")
        except psycopg2.Error as e:
            print("Error executing INSERT query:", e)

    def execute_delete_query(self, query):
        try:
            if not self.connection:
                self.db_connection()

            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            cursor.close()
            print("\033[92mINFO:\033[0m     DELETE query executed successfully!")
        except psycopg2.Error as e:
            print("Error executing DELETE query:", e)

    def execute_update_query(self, query, params=None):
        try:
            if not self.connection:
                self.db_connection()

            cursor = self.connection.cursor()

            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            self.connection.commit()
            cursor.close()
            print("\033[92mINFO:\033[0m     UPDATE query executed successfully!")
        except psycopg2.Error as e:
            print("Error executing UPDATE query:", e)
