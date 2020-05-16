#!/bin/bash

echo 'working'
source ~/.profile
cd /home/ubuntu/spark/bin/
echo 'still working'
spark-submit spark_code.py
