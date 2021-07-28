# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 11:21:53 2021

@author: Роман
"""

a = int(input())
b = int(input())
c = int(input())
d = int(input())

for z in range(c, d + 1):
    print('\t', z, end= '\t')
    if z == d:
        print()
        break
for i in range(a, b + 1):
    print(i, end = '\t')
    for j in range(c, d + 1):
        print(i * j, end = '\t')
    print(end='\n')

        