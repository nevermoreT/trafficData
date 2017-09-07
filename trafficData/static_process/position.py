#doding=utf-8
import pandas as pd 
import re
import sys
import codecs


file=open("kysb.res")
file_new=codecs.open("position.csv","w+","utf-8")
pattern=u"[^a-z0-9\u4e00-\u9fa5.]+"
for line in file:
    temp=line
    temp=line.decode('utf-8')
    s=re.sub(pattern, ',', temp)
    num=len(s)
    s=s[0:num-1]
    s.encode("utf-8")
    file_new.write(s+'\n')
    print s