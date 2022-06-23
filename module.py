from datetime import datetime
import pandas as pd
import os


def get_start_endtime(filename):
        '''
        Get jobid, start time, end time for one darshan log file
        '''
        path = os.popen('cat collect/config.txt | grep darshanlog | cut -d "=" -f2').read().strip()
        f = open(path+'/{}'.format(filename)
        while True:
                line = f.readline().lstrip()
                if not line: break
                linectxt = line.split()
                for _ in linectxt:
                        if 'job' in _: #get jobid
                                jobid = str(linectxt[2])
                        elif 'start_time_' in _: #get start_time and set format to 'YYYY-MM-DD HH:mm:ss'
                                mm = linectxt[3]
                                m = str(datetime.strptime(mm,'%b').month)
                                start = str(linectxt[6]+'-0'+m+'-'+linectxt[4]+' '+linectxt[5])
                        elif 'end_time_' in _ : #get end_time and set format to 'YYYY-MM-DD HH:mm:ss'
                                mm = linectxt[3]
                                m = str(datetime.strptime(mm,'%b').month)
                                end = str(linectxt[6]+'-0'+m+'-'+linectxt[4]+' '+linectxt[5])

        return jobid, start, end

def get_exechost(date, jobid):
        '''
        Printing job id and executing host for one shced log.
        '''

        #schedlog path
        path = os.popen('cat collect/config.txt | grep schedlog | cut -d "=" -f2').read().strip()
        #open daily txt file(YYYYMMDD)
        f = open(path+'/{}'.format(date), 'r')

        while True:
                node = []
                line = f.readline().replace(",","").lstrip()
                if not line: break
                linectxt=line.split()
                for _ in linectxt:
                        if jobid in _ and 'exec_host' in _:
                                node = str(_.replace('+',' ').replace('/0*68',' ')[10:].split())
                        elif jobid in _ :
                                node = None
                        else:
                                raise 'Error. There is no jobid {}'.format(jobid)

        return jobid, node