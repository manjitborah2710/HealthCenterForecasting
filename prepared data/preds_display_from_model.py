import pandas as pd
import numpy as np
from pandas import datetime
from datetime import timedelta
import matplotlib.pyplot as plt
import pickle
from pickle_class_info import SerializableData
f=open("model_urti","rb")
pkl=pickle.load(f)
f.close()
items=pkl.getItems()
label=items[0]
train=items[1]
model=items[2]
preds=model.forecast(11)
preds=preds[0]
last_date=train.index[-1].date()
date_range=last_date
pred_dates=[]
for i in range(len(preds)):
    date_range+=timedelta(weeks=1)
    pred_dates.append(date_range)
pred_dates=pd.DatetimeIndex(pred_dates)
pred_df=pd.DataFrame(data=preds,index=pred_dates,columns=[list(train.columns)[-1]])
total_df_index=pd.DatetimeIndex(train.index.append(pred_df.index))
total_values=train[list(train.columns)[-1]].append(pred_df[list(pred_df.columns)[-1]]).values
total_df=pd.DataFrame(data=total_values,index=total_df_index)

plt.plot(total_df,label='Actual')
plt.plot(pred_df,color='red',label='Predicted')
plt.legend()
plt.show()
