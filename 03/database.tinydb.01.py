from tinydb import TinyDB, Query

database_path = "tinydb.json"
database = TinyDB(database_path)

database.purge_table("items")
table = database.table("items")

table.insert({"name": "Banana", "price": 6000})
table.insert({"name": "Orange", "price": 12000})
table.insert({"name": "Mango", "price": 8400})

print(table.all())


item = Query()

res = table.search(item.name == "Orange")
print("Orange is ", res[0]["price"])

res = table.search(item.price >= 8000)
for i in res:
    print("-", i["name"])
