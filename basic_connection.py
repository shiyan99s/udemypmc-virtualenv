import psycopg2

conn = psycopg2.connect(dbname="postgres", user="postgres", password="786Beefzy", port="5432")
print("connection succesfull")