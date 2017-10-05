import yaml

customer = [
    {
        "name": "dongheon",
        "age": 27,
        "gender": "male"
    },
    {
        "name": "jeongheon",
        "age": 22,
        "gender": "male"
    },
    {
        "name": "kyungmin",
        "age": 55,
        "gender": "female"
    }
]

content = yaml.dump(customer)

# print yaml string in a flow-style
print(content)
