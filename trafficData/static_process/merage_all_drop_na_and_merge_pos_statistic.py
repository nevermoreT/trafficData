#coding=utf-8
import pandas as pd
from pandas import DataFrame
'''
Created on 2017年9月1日

@author: root
'''
#merge all result (by time) into one csv
df=DataFrame()
count=0

#You can change the dir to modify the day you want to process.
rootdir='By10min'
daydir="5_25_10min"
dir=rootdir+'/'+daydir

for num in range(144):
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
        
df_static= df
#fill Na with zero
df_static=df_static.fillna(0)
#merage the pos 
df_pos=pd.read_csv("position.csv")
df_temp=pd.merge(df_pos,df_static,on="监测点id",how="outer")
#print df_temp
#df_temp.to_json("final_result_5_1.json")
df_temp.to_csv("final_result_10min/final_result_{0}.csv".format(daydir),index=False)