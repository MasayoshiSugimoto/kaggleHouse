#!/bin/bash

echo 'test,train' > ../output/score.txt

~/Dev/xgboost/xgboost house.conf task=train 2>&1 \
  | grep rmse \
  | sed -e 's/.*test-rmse://' \
  | tr '\t' ',' \
  | sed -e 's/train-rmse://' >> ../output/score.txt

python plotScore.py
