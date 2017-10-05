import urllib.request as request

filename = "mushroom.csv"
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"

request.urlretrieve(url, filename)
