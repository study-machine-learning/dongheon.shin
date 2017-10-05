import sqlite3

database_path = "db.sqlite"
connection = sqlite3.connect(database_path)

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS items")
cursor.execute("""
    CREATE TABLE items (
        item_id INTEGER PRIMARY KEY,
        name TEXT UNIQUE,
        price INTEGER
    )
""")

connection.commit()


cursor = connection.cursor()

insert_query = "INSERT INTO items (name, price) VALUES(?, ?)"

data = ("Orange", 5200)
cursor.execute(insert_query, data)
connection.commit()


cursor = connection.cursor()

data = [("Mango", 7700), ("Kiwi", 4000), ("Grape", 8000), ("Peach", 9400)]
cursor.executemany(insert_query, data)
connection.commit()


cursor = connection.cursor()

range = (4000, 7000)
cursor.execute("SELECT * FROM items WHERE ? <= price AND price <= ?", range)

items = cursor.fetchall()

for item in items:
    print(item)
