import pandas

def print_data(title, data):

    print("==== {0} ====".format(title))
    print(data)
    print()


series = pandas.Series([1, 3, 5, 7, 9])
print_data("series", series)

data = pandas.DataFrame({
    "height": [170, 180, 155, 143, 154],
    "weight": [80.0, 70.4, 65.5, 45.9, 51.2],
    "type": ["f", "n", "n", "t", "t"]
})

print_data("dataframe", data)
print_data("subframe with a key", data["type"])
print_data("subframe with keys", data[["height", "weight"]])
print_data("subframe with index (1)", data[2:4])
print_data("subframe with index (2)", data[3:])
print_data("subframe with conditions", data[data.height >= 170])

print_data("sort (1)", data.sort_values(by="height"))
print_data("sort (2)", data.sort_values(by="height", ascending=False))

print_data("transpose", data.T)
