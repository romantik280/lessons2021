# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 17:54:09 2021

@author: Роман
"""
with open('../lessons2021/dataset_3363_2 (2).txt') as vhod1:
    vhod = vhod1.readline().strip()


metod = []
metod += vhod
print(metod)
spisok = []
spisok2 = []
bukva = []
cifra = []
for i in range(len(metod)):
    if (metod[i] < 'A') and ((metod[i - 1]) < 'A'):
        spisok2 += metod[i-1] + metod[i]
    elif metod[i] < 'A':
        spisok2 += metod[i]
    else:
        spisok2 += metod[i]
print('spisok2')
print(spisok2)
        
for i in metod:
    if i < 'A':
        spisok += [int(i)]
    else:
        spisok += [i]
print(spisok)

'''for i in range(len(cifra)):
    if cifra[i] == 0:
        cifra[i-1] *= 10




cifra_itog = []
for i in range(len(cifra)):
    if cifra[i] != 0:
        cifra_itog += [cifra[i]]
print(cifra_itog)

a= ''
for i in range(len(bukva)):
    a += str(bukva[i] * cifra_itog[i])

print(a)
with open('../lessons2021/dataset_3363_2 (2).txt', 'w') as vyhod:
    vyhod.write(a)'''