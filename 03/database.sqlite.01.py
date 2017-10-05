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

cursor.execute("INSERT INTO items(name, price) VALUES ('Apple', 800)")
cursor.execute("INSERT INTO items(name, price) VALUES ('Orange', 780)")
cursor.execute("INSERT INTO items(name, price) VALUES ('Banana', 430)")

connection.commit()

cursor = connection.cursor()
cursor.execute("SELECT * FROM items")

for item in cursor.fetchall():
    print(item)
