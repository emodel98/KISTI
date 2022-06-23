#!/bin/sh

#This file should be executed once a day(1AM) with a cron command below
#0 1 * * * /scratch/s5104a11/jwpyo/dailycsv.sh 

path=`cat ./collect/config.txt | grep filepath | cut -d '=' -f2`
cd $path

python3 parse2csv.py
yesterday=$(date +%Y%m%d --date '1 days ago')

#find ./ -name '$yesterday*' -exec rm -f {} \;