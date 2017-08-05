import pandas as panda
import matplotlib.pyplot as pyplot

data = panda.read_csv('../output/score.txt')
pyplot.plot(data['test'], 'r-')
pyplot.plot(data['train'], 'b-')
pyplot.show()
