import urllib.request as request
import os.path
import json

url = "https://api.github.com/repositories"
filename = "data.repositories.json"

if not os.path.exists(filename):
    request.urlretrieve(url, filename)

content = open(filename, "r", encoding="utf-8").read()
items = json.loads(content)

for item in items:
    print(item["name"], " - ", item["owner"]["login"])
