import psycopg2

database = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='123Admin',
    database='jgo_db'
)