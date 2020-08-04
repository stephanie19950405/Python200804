# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:21:16 2020

@author: AE401
"""

import random
num=random.randint(1,10)
x = input("請輸入任意數字")
x =int(x)
while x != num  :
    print("答錯了")
    x=input("請輸入任意數字")
    x = int(x)
if x == num :
    print("答對了")



        
    