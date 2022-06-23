#!/bin/sh

# config
filepath=$(cat config.txt | grep filepath | cut -d '=' -f2)
mkdir -p ${filepath}/D/`hostname`
cd ${filepath}/D/`hostname`
timeset=5
nodename=`hostname | cut -d '0' -f1`

if [[ $nodename == "cpu" ]]
then
        features="branches,branch-misses,bus-cycles,cache-misses,cache-references,cycles,instructions,ref-cycles,alignment-faults,context-switcc
hes,cpu-clock,cpu-migrations,emulation-faults,major-faults,minor-faults,page-faults,task-clock,L1-dcache-load-misses,L1-dcache-loads,L1-dcache--
stores,L1-icache-load-misses,LLC-load-misses,LLC-loads,LLC-store-misses,LLC-stores,branch-load-misses,branch-loads,dTLB-load-misses,dTLB-loads,,
dTLB-store-misses,dTLB-stores,iTLB-load-misses,iTLB-loads,node-load-misses,node-loads,node-store-misses,node-stores,mem-loads,mem-stores"
elif [[ $nodename == "node" ]]
then
        features="branches,branch-misses,bus-cycles,cache-misses,cache-references,cycles,instructions,ref-cycles,alignment-faults,context-switcc
hes,cpu-clock,cpu-migrations,emulation-faults,major-faults,minor-faults,page-faults,task-clock,L1-dcache-load-misses,L1-icache-load-misses,L1-ii
cache-loads,LLC-loads,LLC-stores,branch-load-misses,branch-loads,dTLB-load-misses,iTLB-load-misses,iTLB-loads"
fi
# ------------------------------------- config -------------------------------------


indicator=$( cat ${filepath}/D/indicator.txt )

while [ $indicator -eq 0 ]
do
    if [ $(expr "$(date +%S)" % 10) -eq $timeset ]
    then
        FILE_NAME=$(date '+%Y%m%d%H%M%S')
        sudo perf stat -e  $features  -a -o $FILE_NAME.txt sleep 5


        indicator=$( cat ${filepath}/D/indicator.txt )
    else
        continue
    fi
done

echo "collecting terminated.."