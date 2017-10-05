import json

price = {

    "date": "2017-10-02",
    "price": {
        "Apple": 80,
        "Orange": 55,
        "Banana": 40
    }
}

content = json.dumps(price)
print(content)
