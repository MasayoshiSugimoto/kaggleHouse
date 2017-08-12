import os
import re
import numpy
import pandas
import math
import matplotlib.pyplot as pyplot

######################################################################
# Classes

class XGParam:

    def __init__(self, name, dataType, defaultValue, dataMin, dataMax):
        self.name = name
        self.dataType = dataType
        self.defaultValue = defaultValue
        self.dataMin = dataMin
        self.dataMax = dataMax

    def __str__(self):
        return '{name = %s, dataType = %s, defaultValue = %f dataMin = %f, dataMax = %f}' \
                % (self.name, self.dataType, self.defaultValue, self.dataMin, self.dataMax)

    def getStep(self):
        if math.isnan(self.dataMin):
            return 10
        elif math.isnan(self.dataMax):
            return 10
        return (self.dataMax - self.dataMin) / 1000

    def getStringExpansionCharacter(self):
        if self.dataType == 'double':
            return '%f'
        elif self.dataType == 'long':
            return '%i'


######################################################################
# Global variables

parameters = [XGParam('alpha', 'double', 0.0, 0.0, float('nan')),]

for parameter in parameters:
    print(parameter)

config = numpy.array([0.0])

configFilePath = '../output/tmpConf'

######################################################################
# Functions

def writeLine(outputFile, text):
    outputFile.write(text + "\n")

def generateConfig(configVector):

    outputFile = open(configFilePath, 'w')

    writeLine(outputFile, 'booster = gbtree')
    writeLine(outputFile, 'objective = reg:linear')
    writeLine(outputFile, 'max_depth = 1')
    writeLine(outputFile, 'num_round = 100000')
    writeLine(outputFile, 'save_period = 0')
    writeLine(outputFile, 'data = "../output/train.svm"')
    writeLine(outputFile, 'eval[test] = "../output/test.svm"')
    writeLine(outputFile, 'eval_train = 1')
    writeLine(outputFile, 'test:data = "../output/test.txt"')
    writeLine(outputFile, 'eta = 0.53')
    writeLine(outputFile, 'min_child_weight = 1.5')
    writeLine(outputFile, 'lambda = 0.96')
    writeLine(outputFile, 'tree_method = exact')

    for index in range(len(configVector)):
        parameter = parameters[index]
        formatString = ('%s = ' + parameter.getStringExpansionCharacter())\
                % (parameter.name, configVector[index])
        writeLine(outputFile, formatString)

    outputFile.close()

def train():
    os.system('./train.sh %s' % configFilePath)

def getMinScore():
    return min(pandas.read_csv('../output/score.txt')['test'])

def logScore(parameters, config, minScore):
    log = (parameters[0].getStringExpansionCharacter() + ',%i') % (config[0], minScore)
    resultFile.write(log + '\n')
    print(log)


######################################################################
# Script

os.system('python mapfeat.py')
os.system('python formatData.py')
os.system('python mknfold.py')

generateConfig(config)
train()
minScore = getMinScore()
bestConfig = config[0]
print("minScore=%i" % minScore)

resultFileName = '../output/result.txt'
resultFile = open(resultFileName, 'w')
resultFile.write('parameter,score\n')
logScore(parameters, config, minScore)

for i in range(100):

    config[0] = config[0] + 0.01

    generateConfig(config)
    train()
    newMinScore = getMinScore()
    logScore(parameters, config, newMinScore)

    if newMinScore < minScore:
        minScore = newMinScore
        bestConfig = config[0]

resultFile.close()
print("minScore=%i" % minScore)
print('bestConfig=%f' % bestConfig)

data = pandas.read_csv(resultFileName)
pyplot.plot(data['score'])
pyplot.show()

#os.system('python plotScore.py')
