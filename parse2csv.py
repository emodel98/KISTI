import os
import re
import pandas as pd

host=os.popen('hostname').read().strip()
path = "/scratch/s5104a11/jwpyo/D/{}".format(host)
file_list = [f for f in os.listdir(path) if not f.startswith('.')]
file_list.sort()
print ("file_list: {}".format(file_list))

def timestamp(textfile):
    tm = str(textfile)
    Y = tm[0:4]
    M = tm[4:6]
    D = tm[6:8]
    H = tm[8:10]
    m = tm[10:12]
    s = tm[12:14]
    timestr = Y+'-'+M+'-'+D+' '+H+':'+m+':'+s
    return timestr

def celeminit(dic, time, node): 
    '''
    Initializing CPU(skl nodes) elements dictionary
    '''
    dic={   "time":time,
            "node":node,
            "branches":0,
            "branch_misses":0,
            "bus_cycles":0,
            "cache_misses":0,
            "cache_references":0,
            "cycles":0,
            "instructions":0,
            "ref_cycles":0,
            "alignment_faults":0,
            "context_switches":0,
            "cpu_clock":0,
            "cpu_migrations":0,
            "emulation_faults":0,
            "major_faults":0,
            "minor_faults":0,
            "page_faults":0,
            "task_clock":0,
            "L1_dcache_load_misses":0,
            "L1_dcache_loads":0,
            "L1_dcache_stores":0,
            "L1_icache_load_misses":0,
            "LLC_load_misses":0,
            "LLC_loads":0,
            "LLC_store_misses":0,
            "LLC_stores":0,
            "branch_load_misses":0,
            "branch_loads":0,
            "dTLB_load_misses":0,
            "dTLB_loads":0,
            "dTLB_store_misses":0,
            "dTLB_stores":0,
            "iTLB_load_misses":0,
            "iTLB_loads":0,
            "node_load_misses":0,
            "node_loads":0,
            "node_store_misses":0,
            "node_stores":0,
            "mem_loads":0,
            "mem_stores":0
        }
    return dic

def neleminit(dic, time, node):
    '''
    Initializing NODE(knl nodes) elements dictionary
    '''
    dic={   "time":time,
            "node":node,
            "branches":0,
            "branch_misses":0,
            "bus_cycles":0,
            "cache_misses":0,
            "cache_references":0,
            "cycles":0,
            "instructions":0,
            "ref_cycles":0,
            "alignment_faults":0,
            "context_switches":0,
            "cpu_clock":0,
            "cpu_migrations":0,
            "emulation_faults":0,
            "major_faults":0,
            "minor_faults":0,
            "page_faults":0,
            "task_clock":0,
            "L1_dcache_load_misses":0,
            "L1_icache_load_misses":0,
            "L1_icache_loads":0,
            "LLC_loads":0,
            "LLC_stores":0,
            "branch_load_misses":0,
            "branch_loads":0,
            "dTLB_load_misses":0,
            "iTLB_load_misses":0,
            "iTLB_loads":0,
        }
    return dic


def main():
    mergeddata= []
    for _ in file_list:
        data = open(path+'/'+_ ,'r')
        elem = {}
        time = timestamp(_)
        nodename = host
        print(nodename)
        lines = data.readlines()
        lines = list(map(lambda s: s.rstrip(), lines))
        if nodename.startswith('node'):
            elem = neleminit(elem,time,nodename)
        elif nodename.startswith('cpu'):
            elem = celeminit(elem,time,nodename)

        for i in lines[5:-3]:
            i = i.replace('msec','').replace('-','_').replace(",","")
            content = re.sub(' +', ' ', i)
            spl_cnt = content.split(' ')
            check=spl_cnt[2]
            if check in elem.keys():
                elem[check]=spl_cnt[1]
            else:
                print("The word doesn't exist. Please double check it.")
        data.close()

        mergeddata.append(elem)
    df = pd.DataFrame(mergeddata)
    df.to_csv('/scratch/s5104a11/jwpyo/res/'+host+'/'+str(_)[2:8]+'data.csv', index=False)

if __name__== '__main__':
    main()
