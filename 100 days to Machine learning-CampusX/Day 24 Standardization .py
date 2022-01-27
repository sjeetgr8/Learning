# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 14:09:07 2022

@author: Satya
"""
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler




os.chdir(r'D:\Learning\100-days-of-machine-learning-main\day24-standardization')
df= pd.read_csv('Social_Network_Ads.csv')

df= df.iloc[:,2:]
df.sample(5)

X_train,X_test, Y_train, y_test= train_test_split(df.drop('Purchased',axis=1),
                                                  df['Purchased'],
                                                  test_size=0.3,
                                                  random_state=0)
X_train.shape 
X_test.shape

scaler=StandardScaler()

#fit the scaler to the train set, it will learn the parameters
scaler.fit(X_train)

# transfrom train and test sets
X_train_scaled= scaler.transform(X_train)
X_test_scaled=scaler.transform(X_test)

scaler.mean_

X_train_scaled=pd.DataFrame(X_train_scaled,columns=X_train.columns)
X_test_scaled=pd.DataFrame(X_test_scaled,columns=X_test.columns)

np.round(X_train.describe(),1)

np.round(X_train_scaled.describe(),1)

fig, (ax1, ax2)=plt.subplots(ncols=2,figsize=(12,5))

ax1.scatter(X_train['Age'],X_train['EstimatedSalary'])
ax1.set_title("Before Scaling")
ax2.scatter(X_train_scaled['Age'],X_train_scaled['EstimatedSalary'],color='red')
ax2.set_title("After Scaling")

plt.show()


fig, (ax1, ax2)=plt.subplots(ncols=2,figsize=(12,5))
ax1.set_title("Before Scaling")
sns.kdeplot(X_train['Age'],ax=ax1)
sns.kdeplot(X_train['EstimatedSalary'],ax=ax1)

ax2.set_title('After standard scaling')
sns.kdeplot(X_train_scaled['Age'],ax=ax2)
sns.kdeplot(X_train_scaled['EstimatedSalary'],ax=ax2)
plt.show()


######                    Working Notes                         ########


















































