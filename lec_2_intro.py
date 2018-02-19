#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 19:43:41 2018

@author: andrey
"""

import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm

##Загрузка данных в переменную цифры
digits = datasets.load_digits()

## инициализации классификатора
clf = svm.SVC(gamma=0.01, C=100)

##формирование массивов входных данных и меток
x, y = digits.data[:-10], digits.target[:-10]

##тренировка калссификатора
clf.fit(x,y)

print('Предсказание: ', clf.predict([digits.data[-2]]))

plt.imshow(digits.images[-2], cmap=plt.cm.gray_r, interpolation='nearest')
plt.show()