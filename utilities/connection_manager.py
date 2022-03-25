import os

from psycopg import connect, OperationalError


def create_connection():
    try:

        conn = connect(
            host="trailblazersp1.cf9wrmawv6w7.us-west-1.rds.amazonaws.com",
            dbname="postgres",
            user="teammates",
            password="trailblaze",
            port="5432",
            # host=os.environ.get("HOST"),
            # dbname=os.environ.get("DBNAME"),
            # user=os.environ.get("USER"),
            # password=os.environ.get("PASSWORD"),
            # port=os.environ.get("PORT")
        )
        return conn
    except OperationalError as e:
        raise OperationalError("Could not connect to database")


connection = create_connection()

print(connection)
