# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 19:19:32 2021

@author: Роман
"""

a = [int(i) for i in input().split()]

a = list({x for x in a if a.count(x) > 1})
y = 0
while y < len(a):
    print(a[y], end= ' ')
    y += 1

