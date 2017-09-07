#coding=utf-8
'''
Created on 2017年8月20日

@author: tjx
'''
import os
import re
import time
def  add_meta_data(filename,line):
    with open(filename, 'r+') as f:
        print "Begin to process {0}".format(filename)
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)
        print "Finish to process {0}\n".format(filename)
        f.close()
        
line="车牌号id1,车牌号id2,车牌类型1,车牌类型2,号牌种类,识别时间,上传时间,监测点id,进出口类型,车道id,车身颜色,车辆类型,车标,信息卡编码,违法类型,速度,前端id,行驶方向,图片张数,图片id1,图片id2,图片id3,图片id4,图片id5,前牌是否完成,后牌是否完成,前后牌是否一致,置信度,补传标志,方波长度,分区号,视频URL,保留字段,备用字段1,备用字段2,备用字段3"
dir="/media/tjx/768C23788C2331D3/DataForTraffic/20170511_15/15"
#dir=os.getcwd()
print dir
beginTime=time.time()
print "The program begins at {0} \n".format(beginTime)

for filename in os.listdir(dir):
    filedir=dir+'/'+filename
    f=open(filedir)
    firstline=f.readline()
    #do not reset the metadata
    if not re.match("车牌号id1*", firstline):
        f.close()
        add_meta_data(filedir, line)
    else:
        f.close()
endTime=time.time()
print "The program ends at {0}\n".format(endTime)

print "Use {0} ".format(endTime-beginTime)
#df=pd.read_csv("rImport_rr201705011526_01_4.csv")
#df.info()



