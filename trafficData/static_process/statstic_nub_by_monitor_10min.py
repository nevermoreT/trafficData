#coding=utf-8
'''
Created on 2017年8月20日

@author: tjx
'''
import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import re
import os
import time
def get_csv(dir,pattern):
    """
    Get the .csv file to build pandas DataFrame.
    @param dir:the path of  the csv document;
    @param patton: the re  patton to filter the file;  
    """
    flag=0
    df=DataFrame()
    for  filename in os.listdir(dir):
        if  re.match(pattern, filename):
            filepath=dir+'/'+filename
            try:
                if flag:
                    df=pd.read_csv(filepath)
                    flag=0;
                else:
                    df1=pd.read_csv(filepath)
                    df=pd.concat([df,df1])
            except Exception:
                print filepath+"wrong"
    return df  
                
date="13"
save_path="By10min/5_13_10min"
         
dir="/media/tjx/768C23788C2331D3/DataForTraffic/20170511_15/{0}".format(date)

beginDate=pd.to_datetime("2017/5/{0} 00:00:00".format(date))
endDate=pd.to_datetime("2017/5/{0} 23:50:00".format(date))
zeroTime=pd.to_datetime("2017/5/{0}".format(date))
delta=pd.Timedelta("10 min")
pattern=str()
while beginDate<=endDate:
    beginTime=time.time()
    print "The program begins at {0} \n".format(beginTime)    
    num=int((beginDate-zeroTime)/delta)
    
    if num/6<10:
        pattern="rImport_ysb_201705{0}0{1}{2}[0-9]".format(date,num/6,num%6)
    else:
        pattern="rImport_ysb_201705{0}{1}{2}[0-9]".format(date,num/6,num%6)
    #print pattern
    
    date1=beginDate;
    date2=beginDate+delta        
    df=get_csv(dir, pattern)
    
    df['上传时间']=pd.to_datetime(df['上传时间'])
    df.info()
     
    
    count=df[df['上传时间']>=date1]
    count=df[df['上传时间']<date2]['监测点id'].value_counts()
    a=np.array(count.index)
    result=pd.DataFrame({'监测点id':count.index,'{0}-{1}'.format(date1,date2):count.values})
    #print result
    result.to_csv("{0}/result{1}.csv".format(save_path,num),index=False)
    
    beginDate=beginDate+delta
    
    endTime=time.time()
    print "The program ends at {0}\n".format(endTime)
    print "Use {0} s".format(endTime-beginTime)
    
