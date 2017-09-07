#coding=utf-8
'''
Created on 2017年9月1日

@author: root
'''

import pandas as pd


df_pos=pd.read_csv("position.csv")
df_static=pd.read_csv("final_drop_na.csv")
df_temp=pd.merge(df_pos,df_static,on="监测点id",how="outer")
print df_temp
#df_temp.to_json("final_result_5_1.json")
df_temp.to_csv("final_result_5_1.csv",index=False)