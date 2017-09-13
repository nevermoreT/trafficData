#coding=utf-8
import pandas as pd 
from sklearn import linear_model
from sklearn.ensemble import RandomForestRegressor 
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cross_validation
import sklearn.preprocessing as preprocessing
import seaborn as sns

def do_normalise(im):
    return -np.log(1/((1 + im)/3601) - 1)

def undo_normalise(im):
    return (1/(np.exp(-im) + 1) * 3601 - 1).astype("uint8")

train_df=pd.read_csv("X_default_history.csv")
train_np=train_df.as_matrix()
default=train_df.filter(regex="default*")[:144]
#print default[:144]
X=train_np[:,1:]

y=train_np[:,0]
print y.max()
#print y



clf=linear_model.LinearRegression()
#print cross_validation.cross_val_predict(clf, X, y, cv=5)
#clf=RandomForestRegressor(n_estimators= 60, max_depth=13, min_samples_split=110,
 #                                 min_samples_leaf=20,max_features='sqrt' ,oob_score=True, random_state=10)
#clf = linear_model.LogisticRegression(C=1.0, penalty='l1', tol=1e-6)
clf.fit(X, y)

df=pd.read_csv("add_Week_result/5_21_10min.csv")
last_day_df=pd.read_csv("add_Week_result/5_20_10min.csv")
last_day_row=last_day_df[last_day_df["监测点id"]==10100406]
df_row=df[df["监测点id"]==10100406]
week=df[df["监测点id"]==10100406]["Week"].as_matrix()[0]
last_day_temp=last_day_row.filter( regex="[0-9].*")
df_temp=df_row.filter( regex="[0-9].*")
df_final=pd.DataFrame({"nums":df_temp.T[df_temp.T.columns[0]].as_matrix(),"last_day":last_day_temp.T[last_day_temp.T.columns[0]].as_matrix(),"time_id":range(0,144)},columns=["nums","last_day","time_id"])
df_final.to_csv("temp.csv",index=False)
df_final=pd.read_csv("temp.csv")
df_final['week']=week
#print df_final
dummies_Time=pd.get_dummies(df_final["time_id"], prefix="time_id")
dummies_week=pd.get_dummies(df_final["week"], prefix="week",columns=range(1,8))
df_final= pd.concat([df_final,default], axis=1)
for index ,row in df_final.iterrows():
    if row.time_id>=42 and row.time_id<=54:
        df_final.loc[index,'is_high']=1
    else:
        df_final.loc[index,'is_high']=0

#scaler=preprocessing.StandardScaler()
#default_scale_param = scaler.fit(df_final['default'])
#df_final['default_scaled'] = scaler.fit_transform(df_final['default'], default_scale_param)

df_final= pd.concat([df_final,dummies_Time], axis=1)
df_final.drop(['time_id','week'], axis=1, inplace=True)
df_final['week_1']=0
df_final['week_2']=0
df_final['week_3']=0
df_final['week_4']=0
df_final['week_5']=0
df_final['week_6']=0
df_final['week_7']=0
df_final['week_3']=1
#print df_final
df_final.to_csv("test_final.csv",index=False)
test_np=df_final.as_matrix()
X_test=test_np[:,1:]
y_test=test_np[:,0]

#y_test=do_normalise(y_test)
y_predict=clf.predict(X_test)

df_result=pd.DataFrame({"test":y_test,"pre":y_predict})

df_result.to_csv("result_week_dummied.csv",index=False)
print clf.coef_
sub=df_result['test']-df_result['pre']

score=np.abs(df_result['test']-df_result['pre']/df_result['test']).mean()
print score
fig = plt.figure()
fig.set(alpha=0.2)  # 设定图表颜色alpha参数
df_result['test'].plot()
df_result['pre'].plot()
plt.show()

