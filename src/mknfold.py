import sys
import random

random.seed(10)
nFold=10

inputFile = open('../output/train.txt')
trainFile = open('../output/train.svm', 'w')
testFile = open('../output/test.svm', 'w')

for line in inputFile:
    if random.randint(1, nFold) == 1:
        testFile.write(line)
    else:
        trainFile.write(line)

testFile.close()
trainFile.close()
inputFile.close()
