#coding=utf-8
import pandas as pd 
from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor 
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cross_validation

train_df=pd.read_csv("X_default.csv")
train_np=train_df.as_matrix()
default=train_df.filter(regex="default_*")[:144]
print default[:144]
X=train_np[:,1:]

y=train_np[:,0]
#print y
clf=linear_model.LinearRegression()
print cross_validation.cross_val_predict(clf, X, y, cv=5)
#clf=RandomForestRegressor(n_estimators= 60, max_depth=13, min_samples_split=110,
 #                                 min_samples_leaf=20,max_features='sqrt' ,oob_score=True, random_state=10)
#clf = linear_model.LogisticRegression(C=1.0, penalty='l1', tol=1e-6)
clf.fit(X, y)

df=pd.read_csv("add_Week_result/5_24_10min.csv")
df_row=df[df["监测点id"]==20104605]
week=df[df["监测点id"]==20104605]["Week"].as_matrix()[0]
    
df_temp=df_row.filter( regex="[0-9].*")
df_final=pd.DataFrame({"nums":df_temp.T[df_temp.T.columns[0]],"time_id":range(0,144)})
df_final.to_csv("temp.csv",index=False)
df_final=pd.read_csv("temp.csv")
df_final['week']=week
#print df_final
dummies_Time=pd.get_dummies(df_final["time_id"], prefix="time_id")
dummies_week=pd.get_dummies(df_final["week"], prefix="week",columns=range(1,8))

df_final= pd.concat([df_final,default,dummies_Time], axis=1)
df_final.drop(['time_id','week'], axis=1, inplace=True)
df_final['week_1']=0
df_final['week_2']=0
df_final['week_3']=0
df_final['week_4']=0
df_final['week_5']=0
df_final['week_6']=0
df_final['week_7']=0
df_final['week_3']=1
print df_final
test_np=df_final.as_matrix()
X_test=test_np[:,1:]
y_test=test_np[:,0]
y_predict=clf.predict(X_test)
df_result=pd.DataFrame({"test":y_test,"pre":y_predict})

df_result.to_csv("result_week_dummied.csv",index=False)
print clf.coef_
sub=df_result['test']-df_result['pre']



fig = plt.figure()
fig.set(alpha=0.2)  # 设定图表颜色alpha参数
df_result['test'].plot()
df_result['pre'].plot()
plt.show()
