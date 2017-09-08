#coding=utf-8
import pandas as pd 


df = pd.read_csv("final_result_10min/final_result_5_1_10min.csv")
df['Week']=1
df.to_csv("add_Week_result/5_1_10min.csv",index=False)