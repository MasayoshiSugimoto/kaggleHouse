
def fail(lineIndex, line):
    print('line number = %i' % lineIndex)
    print('line = %s' % line)
    raise Exception("Data error")

FIELD = {
        'index': 0,
        'name': 1,
        'type': 2
    }

features = []
for line in open('../output/featureMap.txt'):
    lineAsArray = line.rstrip().split('\t')
    features.append(lineAsArray)

for filePath in ['../output/test.svm', '../output/train.svm', '../output/test.txt']:

    lineIndex = 0
    for line in open(filePath):
        lineAsArray = line.rstrip().split(' ')

        if (not lineAsArray[0].isdigit()):
            print('first value is not a digit')
            fail(lineIndex, line)

        for columnIndex in range(1, len(lineAsArray)):
            column = lineAsArray[columnIndex]
            if (not column.find(":") > -1):
                print('Incorrect column. columnIndex = %i' % columnIndex)
                print('column = ' + column)
                fail(lineIndex, line)

            if not column.split(':')[0].isdigit():
                print('Column index is not a digit. columnIndex = %i' % columnIndex)
                print('column = ' + column)
                fail(lineIndex, line)

            if not column.split(':')[1].isdigit():
                print('Column value is not a digit. columnIndex = %i' % columnIndex)
                print('column = ' + column)
                fail(lineIndex, line)

            featureIndex = int(column.split(':')[0])
            if featureIndex >= len(features):
                print('Feature index out of bound.')
                print('column = ' + column)
                fail(lineIndex, line)

            featureValue = int(column.split(':')[1])
            if features[featureIndex][FIELD['type']] == 'i' and featureValue != 1:
                print('Enum feature not equal to 1')
                print('column = ' + column)
                fail(lineIndex, line)


        lineIndex += 1
