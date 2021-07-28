# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 12:14:03 2021

@author: Роман
"""
spis = []
slovar = {}
n = int(input())
for i in range(n):
    spis += [input().split(';')]

schet = []
for i in range(n):
    for j in range(0, 4, 2):
        if spis[i][j] not in slovar:
            slovar[spis[i][j]] = schet

a = 0
b = 0
c = 0
d = 0
perem = []
for key in slovar:
    perem += [key]

for z in perem:
    for i in range(n):
        if spis[i][0] == z: #ключ словаря на 1ый в списке игравших
            a += 1
            if int(spis[i][1]) > int(spis[i][3]):
                b += 1
            elif int(spis[i][1]) == int(spis[i][3]):
                c += 1
            elif int(spis[i][1]) < int(spis[i][3]):
                d += 1
       
        
        elif spis[i][2] == z: #ключ словаря на 2ой в списке игравших
            a += 1
            if int(spis[i][1]) < int(spis[i][3]):
                b += 1
            elif int(spis[i][1]) == int(spis[i][3]):
                c += 1
            elif int(spis[i][1]) > int(spis[i][3]):
                d += 1
                
        e = 3 * b + c
        sp = [a, b, c, d, e]
        slovar[z] = sp
    a=0
    b=0
    c=0
    d=0
for key, value in slovar.items():
    print((key + ':'), *value)
    
