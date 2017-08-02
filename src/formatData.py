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
outputFile = open('../output/train.txt', 'w')
header = None
for line in open('../input/train.csv'):

    line = line.rstrip('\n')
    if header is None:
        header = line.split(',')
        continue

    dataRecord = line.split(',')

    #SalePrice is the value to train
    outputFile.write(dataRecord[80]) #SalePrice's index = 80

    for columnIndex in range(1, len(dataRecord)): #Start at 1 to ignore the id

        if columnIndex == 80: #Ignore SalePrice
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

