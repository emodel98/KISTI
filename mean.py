import pandas as pd
from datetime import datetime
from module import get_start_endtime, get_exechost

def main():
        '''
        # Obtain jobid and start/endtime in darshan log. 
        # Use def get_start_endtime() in module.py
        '''
        filename = input()
        jobid, start, end = get_start_endtime(filename) # needs input,,

        '''
        # Identify the node list used by the corresponding jobid from the scheduled log of the date obtained above. 
        # Use def get_start_endtime() in module.py
        '''
        jobid, hostlist = get_exechost(start[:8], jobid) #return jobid, nodelist
        
        '''
        # Open csv of the date and make newdf between start time-10 and end time+10.
        # groupby('{}').mean().format(i) (i is one of the columns in csv) 
        # The average of counts per feature in that time zone is obtained. 
        # save each rows in csv
        # index = jobid, nodename / column = each feature
        '''
        for i in range(len(hostlist)): #for all host list for one jobid
                bound = datetime.timedelta(seconds=10)
                path1 = '/scratch/s5104a11/jwpyo/res/{}/{}res.csv'.format(hostlist[i],start[2:8])
                df1 = pd.read_csv(path1,'/','')
                df1['timestamp'] = pd.to_datetime(df1['timestamp'], infer_datetime_format=True)

                if start[8]==end[8]:
                        mask = (df1['timestamp'] > start - bound) & (df1['timestamp'] < end + bound)
                        selected_df = df1.loc[mask]
                else: 
                        path2 = '/scratch/s5104a11/jwpyo/res/{}/{}data.csv'.format(hostlist[i],end[2:8])
                        df2 = pd.read_csv(path2)
                        df2['timestamp'] = pd.to_datetime(df1['timestamp'], infer_datetime_format=True)
                        mask1 = (df1['timestamp'] > start - bound)
                        mask2 = (df2['timestamp'] < end + bound)
                        selected_df = pd.concat(df1.loc[mask1],df2.loc[mask2])

                # get mean, std ... of each features per one node that is used
                print( hostlist[i],':\n', selected_df.describe() ) 
        
        
if __name__== '__main__':
    main()
