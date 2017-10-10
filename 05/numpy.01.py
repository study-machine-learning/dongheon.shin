import numpy as np

def print_data(title, data):

    print("==== {0} ====".format(title))
    print(data)
    print()


zeros = np.zeros(10, dtype=np)
print_data("zeros", zeros)

ones = np.ones(10, dtype=np)
print_data("ones", ones)

numbers = np.arange(10, dtype=np.uint64)
print_data("numbers", numbers)

multiply = numbers * 3
print_data("multiply", multiply)

mean = numbers.mean()
print_data("mean", mean)
