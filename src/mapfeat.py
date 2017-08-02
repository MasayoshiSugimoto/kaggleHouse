#!/usr/bin/python

import os

if not os.path.exists('../output'):
    os.makedirs('../output')

outputFile = open('../output/featureMap.txt', 'w')

dataType = ''
featureCounter = 0
featureId = 'featureId'
for line in open('../input/data_description.txt'):
    if line.isspace():
        continue

    if line[0].isspace():
        featureId = line.lstrip().split('\t')[0]
        outputFile.write('%i\t%s=%s\ti\n' % (featureCounter, dataType, featureId) )
        featureCounter += 1
        lastBranch = 1
    else:
        if featureId == '':
            outputFile.write('%i\t%s\t%s\n' % (featureCounter, dataType, 'int') )
            featureCounter += 1
        featureId = ''
        dataType = line.split(':')[0]

#Write the last element if it has not been written
if featureId == '':
    outputFile.write('%i\t%s\t%s\n' % (featureCounter, dataType, 'int') )

outputFile.close()
