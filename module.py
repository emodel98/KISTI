from datetime import datetime
import pandas as pd


def get_start_endtime(filename):
        '''
        Get jobid, start time, end time for one darshan log file
        '''
        path = '/scratch/s5104a11/jwpyo/res/darshanlog'
        f = open(path+'/'+'{}.txt'.format(filename), 'r')
        while True:
                line = f.readline().lstrip()
                if not line: break
                linectxt = line.split()
                for _ in linectxt:
                        if 'job' in _: #get jobid
                                jobid = str(linectxt[2])
                                #print('jobid: '+jobid)
                        elif 'start_time_' in _: #get start_time and set format to 'YYYY-MM-DD HH:mm:ss'
                                mm = linectxt[3]
                                m = str(datetime.strptime(mm,'%b').month)
                                start = str(linectxt[6]+'-0'+m+'-'+linectxt[4]+' '+linectxt[5])
                                #print('start at: '+ start)
                        elif 'end_time_' in _ : #get end_time and set format to 'YYYY-MM-DD HH:mm:ss'
                                mm = linectxt[3]
                                m = str(datetime.strptime(mm,'%b').month)
                                end = str(linectxt[6]+'-0'+m+'-'+linectxt[4]+' '+linectxt[5])
                                #print('end at: '+ end)
        return jobid, start, end # array? list? dict? 원하는 형식이 어떤 건지에 따라..

def get_exechost(date, jobid):
        '''
        Printing job id and executing host for one shced log.
        '''

        #schedlog path
        path='/scratch/s5104a11/jwpyo/res/schedlog'
        #open daily txt file(YYYYMMDD)
        f = open(path+'/'+'{}.txt'.format(date), 'r')

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