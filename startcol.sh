#!/bin/sh

#start collecting data for all nodes
filepath=$(cat config.txt | grep filepath | cut -d '=' -f2)
echo '0' > $filepath/D/indicator.txt

ssh cpu0001 "nohup /scratch/s5104a11/jwpyo/collect/collect_master_0sec.sh > /dev/null 2>&1 &"
ssh cpu0001 "nohup /scratch/s5104a11/jwpyo/collect/collect_master_5sec.sh > /dev/null 2>&1 &"
ssh node0001 "nohup /scratch/s5104a11/jwpyo/collect/collect_master_0sec.sh > /dev/null 2>&1 &"
ssh node0001 "nohup /scratch/s5104a11/jwpyo/collect/collect_master_5sec.sh > /dev/null 2>&1 &"