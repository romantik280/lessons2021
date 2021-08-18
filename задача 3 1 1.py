# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 13:42:55 2021

@author: Роман
"""

s = input()
t = input()

usl = 1
count = 0

while usl != -1:
    usl = s.find(t)
    if usl >= 0:
        count += 1
    s = s[usl + 1:]
print(count)