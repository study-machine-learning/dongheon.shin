from sklearn import svm, metrics
from os import makedirs

import urllib.request as request
import urllib.parse as parse
import gzip
import os
import os.path
import struct


baseurl = "http://yann.lecun.com/exdb/mnist/"

dirpath = "./mnist/handwriting/"
files = [
    "train-images-idx3-ubyte.gz",
    "train-labels-idx1-ubyte.gz",
    "t10k-images-idx3-ubyte.gz",
    "t10k-labels-idx1-ubyte.gz",
]


def to_csv(name, max):

    image_file = open(dirpath + name + "-images-idx3-ubyte", "rb")
    label_file = open(dirpath + name + "-labels-idx1-ubyte", "rb")

    csv = open(parse.urljoin(dirpath, name + ".csv"), "w", encoding="utf-8")

    # read meta information from files
    magic, label_count = struct.unpack(">II", label_file.read(8))
    magic, image_count = struct.unpack(">II", image_file.read(8))

    # read counts of rows and columns
    rows, columns = struct.unpack(">II", image_file.read(8))
    pixels = rows * columns

    for index in range(label_count):

        # restrict learning
        if index > max:
            break

        # read data as unsigned binary
        label = struct.unpack("B", label_file.read(1))[0]

        # read binary data and convert to string
        bdata = image_file.read(pixels)
        sdata = list(map(lambda n: str(n), bdata))

        # make string data as csv
        csv.write(str(label) + ",")
        csv.write(",".join(sdata) + "\n")

        # save as an image for test
        if index < 10:

            sample = "P2 28 28 255\n"
            sample += " ".join(sdata)

            holder = "{0}-{1}-{2}.pgm"

            output = parse.urljoin(dirpath, holder.format(name, index, label))
            with open(output, "w", encoding="utf-8") as fp:
                fp.write(sample)

    csv.close()

    label_file.close()
    image_file.close()


def load_csv(filename):

    labels = []
    images = []

    with open(filename, "r") as fp:

        for line in fp:

            columns = line.split(",")

            if len(columns) < 2:
                continue

            # add label and convert data to unit vectors
            labels.append(int(columns.pop(0)))
            values = list(map(lambda n: int(n) / 256, columns))

            images.append(values)

    return {"labels": labels, "images": images}


if not os.path.exists(dirpath):
    makedirs(dirpath)

# download files
for f in files:

    url = parse.urljoin(baseurl, f)
    location = parse.urljoin(dirpath, f)

    if not os.path.exists(location):
        request.urlretrieve(url, location)

# unzip downloaded files
for f in files:

    gz_file = parse.urljoin(dirpath, f)
    raw_file = gz_file.replace(".gz", "")

    if not os.path.exists(raw_file):
        with gzip.open(gz_file, "rb") as rfp:
            body = rfp.read()
            with open(raw_file, "wb") as wfp:
                wfp.write(body)

to_csv("train", 5000)
to_csv("t10k", 500)

data = load_csv(parse.urljoin(dirpath, "train.csv"))
test = load_csv(parse.urljoin(dirpath, "t10k.csv"))

classifier = svm.SVC()
classifier.fit(data["images"], data["labels"])

predict = classifier.predict(test["images"])

score = metrics.accuracy_score(test["labels"], predict)
report = metrics.classification_report(test["labels"], predict)

print("score = ", score)
print("report")
print(report)
