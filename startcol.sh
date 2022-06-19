#!/bin/sh

#start collecting data for all nodes

echo '0' > /scratch/s5104a11/jwpyo/D/indicator.txt

ssh cpu0001 "nohup /scratch/s5104a11/jwpyo/collect/cpu_0sec.sh > /dev/null 2>&1 &"
ssh cpu0001 "nohup /scratch/s5104a11/jwpyo/collect/cpu_5sec.sh > /dev/null 2>&1 &"
ssh node0001 "nohup /scratch/s5104a11/jwpyo/collect/node_0sec.sh > /dev/null 2>&1 &"
ssh node0001 "nohup /scratch/s5104a11/jwpyo/collect/node_5sec.sh > /dev/null 2>&1 &"