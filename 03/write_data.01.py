filename = "a.bin"
data = 100

with open(filename, "wb") as fp:
    fp.write(bytearray([data]))
