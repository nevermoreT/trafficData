#coding=utf-8
import  pandas as pd
import matplotlib.pyplot as plt
from pandas import  DataFrame,Series
import numpy as np
'''
Created on 2017年9月4日

@author: root
'''

fig=plt.figure()
fig.set(alpha=0.2)
data=pd.read_csv("final_result_5_1.csv")
data=data.filter(regex='监测点id|[0-9].*')
series= data[data['监测点id']==10100406].filter(regex="[0-9].*")

array=series.as_matrix()
array=array.reshape(46,1)

print array
plt.plot(array)
plt.show()

