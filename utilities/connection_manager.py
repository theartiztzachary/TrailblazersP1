from psycopg import connect, OperationalError
import os

def create_connection():
    try:
        conn = connect(
            host=os.environ.get("HOST"),
            dbname=os.environ.get("DBNAME"),
            user=os.environ.get("USER"),
            password=os.environ.get("PASSWORD"),
            port=os.environ.get("PORT")
        )
        return conn
    except OperationalError:
        print("Something went wrong with the connection.")

connection = create_connection()

print(connection)