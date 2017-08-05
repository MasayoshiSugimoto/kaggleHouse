#!/bin/bash

outputFile="../output/submission.csv"

echo 'Id,SalePrice' > $outputFile
cat pred.txt | awk 'BEGIN{i=1461} {print i","$0; i++}' >> $outputFile
