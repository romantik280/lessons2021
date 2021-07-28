# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 13:38:50 2021

@author: Роман
"""

a1 = input()
a2 = input()
a3 = input()
a4 = input()


zasifr = {}
for i in range(len(a1)):
    zasifr[a1[i]] = a2[i]


razsifr = {}
for i in range(len(a2)):
    razsifr[a2[i]] = a1[i]


for j in a3:
    print(zasifr[j], end='')
print()
for j in a4:
    print(razsifr[j], end='')