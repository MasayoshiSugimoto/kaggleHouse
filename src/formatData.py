FIELD = {
        'index': 0,
        'name': 1,
        'type': 2
    }

#Load the feature map
featureMap = {}
for line in open('../output/featureMap.txt'):
    feature = line.rstrip('\n').split('\t')
    featureMap[feature[FIELD['name']]] = feature

#Convert the train data in SVMlib format
#The training index is the index we want to predict. Set to 0 for test data.
def format(inputFilePath, outputFilePath, trainingIndex):
    outputFile = open(outputFilePath, 'w')
    header = None
    for line in open(inputFilePath):

        line = line.rstrip('\n')
        if header is None:
            header = line.split(',')
            continue

        dataRecord = line.split(',')

        #SalePrice is the value to train
        outputFile.write(dataRecord[trainingIndex])

        for columnIndex in range(1, len(dataRecord)): #Start at 1 to ignore the id

            if columnIndex == trainingIndex: #Ignore training data
                continue

            columnName = header[columnIndex]
            value = dataRecord[columnIndex]

            #Ignore not applicable value and treat it as a missing value
            if value == 'NA':
                continue

            #Get the feature for the column
            if featureMap.has_key(columnName): #For int, the feature name is the column name
                feature = featureMap[columnName]
            else: #For enumerations, the feature name is <columnName>=<value>
                feature = featureMap[columnName + "=" + value]

            outputFile.write(' ')
            if feature[FIELD['type']] == 'int':
                outputFile.write(feature[FIELD['index']] + ":" + value)
            elif feature[FIELD['type']] == 'i':
                outputFile.write(feature[FIELD['index']] + ':1')
            else:
                raise Exception('Undefined field type: "' + feature[FIELD['type']] + '"')

        outputFile.write('\n')

    outputFile.close()

format('../input/train.csv', '../output/train.txt', 80)
format('../input/test.csv', '../output/test.txt', 0)
