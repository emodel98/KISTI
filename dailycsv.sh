#!/bin/sh


#need to run once a day..

cd /scratch/s5104a11/jwpyo

python3 parse2csv.py
yesterday=$(date +%Y%m%d --date '1 days ago')
echo    $yesterday
#rm ./D/$yesterday*