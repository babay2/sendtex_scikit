#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 06:36:43 2018

@author: andreyb
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from matplotlib import style

style.use('ggplot')

x = [1,5,1.5,8,1,9]
y = [2,8,1.8, 8, 0.6,11]

#plt.scatter(x, y)
#plt.show()

X = []
for i in range(len(x)):
    X.append([x[i], y[i]])
X =np.array(X)

Y = [0,1,0,1,0,1]

clf = svm.SVC(kernel='linear', C=1.0)
clf.fit(X,Y)

print(clf.predict([[0.57, 0.76]]))

#w = clf.coef_[0]
#print(w)

#a = -w[0] / w[1]
#xx = np.linspace(0,12)
#yy = a * xx - clf.intercept_[0] / w[1]
#
#h0 = plt.plot(xx, yy, 'k-', label='не взвешеное деление')
#plt.scatter(X[:,0], X[:, 1], c=Y)
#plt.legend()
#plt.show()