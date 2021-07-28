# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 14:17:59 2021

@author: Роман
"""
matr = []
a = [0]
b = []
while a[0] != 'end':
    a = [i for i in input().split()]
    matr += [a]
print(matr)
m = len(matr[0])
n= len(matr) - 1
print(n, m)
matr2 = matr[0:m]
print(matr2)
for i in range(n):
    for j in range(m):
        if n == 1:
            if m == 1:
                b[i][j] = int(matr2[i][j])*2 + int(matr2[i-1][j]) + int(matr2[i+1][j])
            b[i][j] = int(matr2[i][j])*2 + int(matr2[i-1][j]) + int(matr2[i+1][j])
print(b)