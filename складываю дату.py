# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 15:32:30 2021

@author: Роман
"""

vhod = [int(i) for i in input().split()]
days = int(input())

a = vhod[0]
b = vhod[1]
c = vhod[2]
import datetime
first_date = datetime.date(a, b, c)
second_date = first_date + datetime.timedelta(days = days)

print(second_date.year, second_date.month, second_date.day)
