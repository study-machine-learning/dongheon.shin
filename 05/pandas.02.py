import pandas

def normalize(data, key):

    column = data[key]

    max_value = column.max()
    min_value = column.min()

    data[key] = (column - min_value) / (max_value - min_value)

frame = pandas.DataFrame({
    "height": [170, 180, 155, 143, 154, 160],
    "weight": [80.0, 70.4, 65.5, 45.9, 51.2, 72.5],
    "gender": ["f", "m", "m", "f", "f", "m"]
})

normalize(frame, "height")
normalize(frame, "weight")

print(frame)
