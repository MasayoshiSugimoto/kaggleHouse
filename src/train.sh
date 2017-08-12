#!/bin/bash

configFile=$1

if [ "$configFile" = "" ]
then
  configFile=house.conf
fi

echo 'test,train' > ../output/score.txt

~/Dev/xgboost/xgboost $configFile task=train 2>&1 \
  | grep rmse \
  | sed -e 's/.*test-rmse://' \
  | tr '\t' ',' \
  | sed -e 's/train-rmse://' >> ../output/score.txt

