import matplotlib.pyplot as pyplot
import pandas

table = pandas.read_csv("bmi.csv", index_col=2)

figure = pyplot.figure()
aux = figure.add_subplot(1, 1, 1)


def scatter(label, color):

    bmi = table.loc[label]
    aux.scatter(bmi["weight"], bmi["height"], c=color, label=label)


scatter("fat", "red")
scatter("normal", "yellow")
scatter("thin", "purple")

aux.legend()

pyplot.savefig("bmi.png")
pyplot.show()
