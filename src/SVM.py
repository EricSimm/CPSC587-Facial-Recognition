# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 12:37:39 2017

@author: Administrator
"""

import numpy as np
from sklearn import preprocessing, cross_validation, neighbors, svm
import pandas as pd
from sklearn.externals import joblib

df = pd.read_csv('E:\\test.csv',header=None)
df.replace('?',-99999, inplace=True)
X = np.array(df[df.columns[1:129]])
X.reshape(-1,1)
y = np.array(df[df.columns[0]])
print(X)

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clt = svm.LinearSVC()

clt.fit(X_train,y_train)
confidence = clt.score(X_test, y_test)
print(confidence)
if confidence>0.97:
    joblib.dump(clt, 'E:\\SVMModel.pkl') 