# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 12:16:44 2021

@author: Роман
"""
m=1
i=0
j=1
s = input()
while j < (len(s)):
    if s[i] != s[j]:       
        print(str(s[i]), end='')
        print(m, end='')
        i+=1
        j+=1
        m=1
    else:
        m+=1
        i+=1
        j+=1
print(str(s[i]), end='')
print(m)

        
       

