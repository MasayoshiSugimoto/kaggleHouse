#!/bin/bash

#Create train and test data set in svm format
python mapfeat.py
python formatData.py
python mknfold.py

#Training the output model
~/Dev/xgboost/xgboost house.conf
#Output prediction of test data
~/Dev/xgboost/xgboost house.conf task=pred model_in=0002.model
#Print the boosters of 0002.model in dump.raw.txt
#~/Dev/xgboost/xgboost house.conf task=pred model_in=0002.model name_dump=../output/dump.raw.txt
#Print the boosters of 0002.model in dump.nice.txt with feature map
~/Dev/xgboost/xgboost house.conf task=dump model_in=0002.model fmap=../output/featureMap.txt name_dump=dump.nice.txt

cat dump.nice.txt

./createSubmission.sh
