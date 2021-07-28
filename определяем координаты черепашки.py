# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 18:06:59 2021

@author: Роман
"""

komanda = []
n= int(input())
komanda += [input().split(' ') for i in range(n)]

kord = {'север': 0, 'юг': 0, 'восток': 0, 'запад': 0}

for i in range(len(komanda)):
    if komanda[i][0] in kord:
        a = int(komanda[i][1])
        kord[komanda[i][0]] += a
        
x = kord['восток'] - kord['запад']
y = kord['север'] - kord['юг']
print(x, y)
