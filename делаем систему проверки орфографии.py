# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 15:16:14 2021

@author: Роман
"""


a= []
b= []
n = int(input())
for i in range(n):
    a += [input().lower()]
m = int(input())
for j in range(m):
    b += [input().lower().split(' ')]

s = set()

for i in range(len(b)):
    for j in range(len(b[i])):
        if b[i][j] not in a:
            s.add(b[i][j])
for i in s:
    print(i)
