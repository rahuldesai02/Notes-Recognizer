#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 19:56:47 2018

@author: shashi
"""
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix
scaler = StandardScaler()
clf = MLPClassifier(hidden_layer_sizes=(5))
data = np.load('Data.npy')
X = [x[:-1] for x in data]
y = [x[-1] for x in data]
scaler.fit(X)
X = scaler.transform(X)
clf.fit(X,y)
predictions = clf.predict(X)
print(confusion_matrix(y,predictions))
weights = clf.coefs_