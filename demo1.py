import psycopg2

def createTable():

    conn = psycopg2.connect(dbname = "postgres", user = "postgres", password = "786Beefzy", port = "5432")
    print("connection successful")
    curr = conn.cursor()
    curr.execute('''CREATE TABLE demo1(ID SERIAL, NAME TEXT, AGE INT, ADDRESS TEXT);''')
    print("Table created")
    conn.commit()
    conn.close()

def insertData():
    conn = psycopg2.connect(dbname = "postgres", user = "postgres", password = "786Beefzy", port = "5432")
    print("connection successful")
    curr = conn.cursor()
    curr.execute('''INSERT INTO demo1(NAME, AGE, ADDRESS) VALUES ('Shiyan', 21, 'NDLS');''')
    conn.commit()
    conn.close()

def insertSoftcoreData():
    conn = psycopg2.connect(dbname = "postgres", user= "postgres", password = "786Beefzy", port = "5432")
    curr = conn.cursor()
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    address = input("Enter address :")
    query = '''INSERT INTO demo1(NAME, AGE, ADDRESS) VALUES (%s,%s,%s);'''
    curr.execute(query,(name, age, address))
    print("successfully inserted")
    conn.commit()
    conn.close()

  
# createTable()
# insertData()
insertSoftcoreData()