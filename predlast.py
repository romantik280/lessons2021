# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 14:33:58 2021

@author: Роман
"""
import pandas as pd
data = pd.read_csv('dataset_3380_5.txt', delimiter='	', header = None)
data2 = pd.DataFrame(data)
data2.columns = ['class', 'sec_name', 'hight']

X = data2.drop(['sec_name'], axis=1)
a = X.groupby('class').mean()
print(data)
print(a)