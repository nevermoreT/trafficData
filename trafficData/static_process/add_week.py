#coding=utf-8
import pandas as pd 


df = pd.read_csv("final_result_10min/final_result_5_25_10min.csv")
df['Week']=4
df.to_csv("add_Week_result/5_25_10min.csv",index=False)