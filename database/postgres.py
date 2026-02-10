import psycopg2

def get_conn():
    return psycopg2.connect(
        dbname="btts",
        user="postgres",
        password="password",
        host="localhost"
    )
