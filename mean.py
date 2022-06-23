import pandas as pd
import os
from datetime import datetime
from module import get_start_endtime, get_exechost

def main():
        '''
        From darshan log, jobid, starttime, endtime are gathered with get_start_endtime() from module.py.
        '''
        print('please input darshan log file name')
        filename = input() # Manual input the name we want to analyze
        jobid, start, end = get_start_endtime(filename)

        '''
        Get nodelist used by the corresponding jobid from the scheduled log of the date obtained above. 
        get_start_endtime() from  module.py
        '''
        jobid, hostlist = get_exechost(start[:8], jobid) #return jobid, nodelist

        '''
        # Open csv of the date and make newdf between start time-10 and end time+10.
        # groupby('{}').mean().format(feature) 
        # The average of counts per feature in the time period is obtained.
        # save one row in (csv/DB) 
        # index = jobid, nodename / column = each feature
        '''
        for i in range(len(hostlist)): #for all host list for one jobid
                bound = datetime.timedelta(seconds=10)
                path1 = str(os.getcwd())+'/res/{}/{}data.csv'.format(hostlist[i],start[2:8])
                df1 = pd.read_csv(path1,'/','')
                df1['timestamp'] = pd.to_datetime(df1['timestamp'], infer_datetime_format=True)

                if start[8]==end[8]:
                        mask = (df1['timestamp'] > start - bound) & (df1['timestamp'] < end + bound)
                        selected_df = df1.loc[mask]
                else:
                        path2 = str(os.getcwd())+'/res/{}/{}data.csv'.format(hostlist[i],end[2:8])
                        df2 = pd.read_csv(path2)
                        df2['timestamp'] = pd.to_datetime(df1['timestamp'], infer_datetime_format=True)
                        mask1 = (df1['timestamp'] > start - bound)
                        mask2 = (df2['timestamp'] < end + bound)
                        selected_df = pd.concat(df1.loc[mask1],df2.loc[mask2])

                # get mean, std of each feature per one node that is used. save each row in csv
                print( hostlist[i],':\n', selected_df.describe() )


if __name__== '__main__':
    main()
                           