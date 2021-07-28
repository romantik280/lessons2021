# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 16:20:42 2021

@author: Роман
"""

a = float(input())
b = float(input())
c = str(input())
if c == '+':
    print(a + b)
elif c == '-':
    print(a-b)
elif (c == '/' or c == 'mod' or c == 'div') and b == 0:
    print('Деление на 0!')
elif c == '/':
    print(a / b)
elif c == '*':
    print(a * b)
elif c == 'mod':
    print(a % b)
elif c == 'pow':
    print(a ** b)
elif c == 'div':
    print(a // b)

