import MySQLdb

connection = MySQLdb.connect(
    user="user",
    passwd="user_password",
    host="localhost",
    db="ml"
)

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS items")
cursor.execute("""
    CREATE TABLE items (
        item_id INTEGER PRIMARY KEY AUTO_INCREMENT,
        name TEXT,
        price INTEGER
    )
""")


items = [("Banana", 300), ("Mango", 640), ("Kiwi", 280)]
for item in items:
    cursor.execute("INSERT INTO items(name, price) VALUES (%s, %s)", item)

cursor.execute("SELECT * FROM items")
for row in cursor.fetchall():
    print(row)
