#!/bin/sh
cd /scratch/s5104a11/jwpyo/D/cpu0001

indicator=$( cat /scratch/s5104a11/jwpyo/D/indicator.txt )
while [ $indicator -eq 0 ]
do
    if [ $(expr "$(date +%S)" % 10) -eq 0 ]
    then
        FILE_NAME=$(date '+%Y%m%d%H%M%S')
        sudo perf stat -e  branches,branch-misses,bus-cycles,cache-misses,cache-references,cycles,instructions,ref-cycles,alignment-faults,context-switches,cpu-clock,cpu-migrations,emulation-faults,major-faults,minor-faults,page-faults,task-clock,L1-dcache-load-misses,L1-dcache-loads,L1-dcache-stores,L1-icache-load-misses,LLC-load-misses,LLC-loads,LLC-store-misses,LLC-stores,branch-load-misses,branch-loads,dTLB-load-misses,dTLB-loads,dTLB-store-misses,dTLB-stores,iTLB-load-misses,iTLB-loads,node-load-misses,node-loads,node-store-misses,node-stores,mem-loads,mem-stores  -a -o $FILE_NAME.txt sleep 5
        indicator=$( cat /scratch/s5104a11/jwpyo/D/indicator.txt )
    else
        continue
    fi
done
echo "collecting terminated.."