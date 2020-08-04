# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 11:32:44 2020

@author: AE401
"""

import random
num=random.randint(1,20)
x = input("請輸入任意數字")
x =int(x)
y=0
while y<5:
    if x !=num:
        print("答錯了")
        x=input("請輸入任意數字")
        x = int(x)
        y=y+1
print("end")