#coding=utf-8
import pandas as pd
from pandas import DataFrame,Series
import os
'''
Created on 2017年9月1日

@author: root
'''
df=DataFrame()
count=0
dir="5_2"
for num in range(48):
    file=dir+'/result{0}.csv'.format(num)
    try:
        if  count==0:
            df=pd.read_csv(file)
        else:
            temp=pd.read_csv(file)
            df=pd.merge(df,temp,on="监测点id",how='outer')
        count+=1
    except IOError:
        print "no file {0}".format(file)
           
df.to_csv("final5_2.csv",index=False)


        
        
    


