# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 10:00:12 2021

@author: Роман
"""
list = []
with open('dataset_24465_4.txt') as a:
    for line in a:
        list += [line]

list2 = []
list2 = list[::-1]
print(list)
print(list2)


with open('out1.txt', 'a') as w:
    for i in list2:
        
        w.write(i)
        
