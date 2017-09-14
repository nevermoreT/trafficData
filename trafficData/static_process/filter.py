#coding=utf-8
import numpy as np
import pandas as pd
'''
Created on 2017年9月13日

@author: root
'''

def smooth(y,a):
    s0=y[:3].mean()
    s=[]
    for i in range(len(y)):
        if i==0:
            s.append(y[i]*a+(1-a)*s0)
        else:
            s.append(y[i]*a+(1-a)*s[-1])
    return np.array(s)

if __name__=="__main__":
    y=np.array(range(10))
    print smooth(y, 0.5)
    