# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 18:40:02 2021

@author: Роман
"""
'''
import simplecrypt
with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()
codes = open('passwords.txt')

a= simplecrypt.decrypt(encrypted)
print(a)
'''
import requests
from simplecrypt import decrypt, DecryptionException
 
code = requests.get('https://stepic.org/media/attachments/lesson/24466/encrypted.bin').content
passes = requests.get('https://stepic.org/media/attachments/lesson/24466/passwords.txt').content
 
for p in passes.split():
    try:
        s = decrypt(p, code)
    except DecryptionException:
        pass
    else:
        print(p, s)