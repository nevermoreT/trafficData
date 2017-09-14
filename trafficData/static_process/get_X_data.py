#coding=utf-8
'''
Created on 2017年9月9日

@author: root
'''
import pandas as pd 
import os
import matplotlib.pyplot as plt
import sklearn.preprocessing as preprocessing
from pandas import Series
import numpy as np
import seaborn as sns 
import filter
last_day=Series()
df_final=pd.DataFrame()
for filename in os.listdir("add_Week_result"):
    df=pd.read_csv("add_Week_result/"+filename)
    
    df_row=df[df["监测点id"]==20104605]
    week=df[df["监测点id"]==20104605]["Week"].as_matrix()[0]
    
    df_temp=df_row.filter( regex="[0-9].*")
    df_new=pd.DataFrame({"nums":df_temp.T[df_temp.T.columns[0]].as_matrix(),"time_id":range(0,144)})
    df_new['week']=week
    if  not last_day.empty:
        df_new['last_day']=last_day
        last_day=df_new['nums']
    else:
        df_new['last_day']=df_new['nums']
        last_day=df_new['nums']
        #print 

    #print df_new
    if not df_final.empty:
        df_final=pd.concat([df_final,df_new])
    else:
        df_final=df_new

df_final.to_csv("temp.csv",index=False)
df_final=pd.read_csv("temp.csv")
meanList=[]
for i in range(0,144):
    meanList.append(df_final[df_final.time_id==i].nums.mean())

print meanList
for index ,row in df_final.iterrows():
    df_final.loc[index,'default']=meanList[df_final['time_id'][index]]
    if row.time_id>=42 and row.time_id<=54:
        df_final.loc[index,'is_high']=1
    else:
        df_final.loc[index,'is_high']=0
        

dummies_Time=pd.get_dummies(df_final["time_id"], prefix="time_id")
dummies_week=pd.get_dummies(df_final["week"], prefix="week")
df_final= pd.concat([df_final,dummies_Time,dummies_week], axis=1)
df_final.drop(['time_id','week'], axis=1, inplace=True)

a=df_final.as_matrix()
df_final=df_final[df_final.nums>0]
df_final=df_final[df_final.nums<1000]
df_final['nums']=filter.smooth(df_final['nums'].as_matrix(),0.1)
df_final.to_csv("X_default_history.csv",index=False)

fig = plt.figure()
fig.set(alpha=0.2)  # 设定图表颜色alpha参数
df_final['nums'].plot()
plt.plot(filter.smooth(df_final['nums'].as_matrix(), 0.5))
plt.show()

