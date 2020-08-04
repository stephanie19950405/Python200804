# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 09:57:39 2020

@author: AE401
"""

import random
num=random.randint(1,10)
x=input("請輸入任意數字")
if x==num:
    print("猜對了!")
else:
    print("猜錯了!")