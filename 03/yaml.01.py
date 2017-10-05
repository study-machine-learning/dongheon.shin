import yaml

content = """
Date: 2017-10-02
PriceList:
    -
        item_id: 1000
        name: Banana
        color: yellow
        price: 800
    -
        item_id: 1001
        name: Orange
        color: orange
        price: 1400
    -
        item_id: 1002
        name: Apple
        color: red
        price: 2400
"""

items = yaml.load(content)

for item in items["PriceList"]:
    print(item["name"], item["price"])
