# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 15:45:43 2020

@author: AE401
"""

ns=[]
ss=[]

total=0
average=0

p=input("請輸入人數")
p=int(p)

#人名和分數
for k in range(p):
    s=input("請輸入分數")
    s=int
    ss.append(s)
    n=input("請輸入名字")
    ns.append(n)
    
#總分平均
for k in range(p):
    total=total+ss(k)
    average=(total/p)
print("total is",total)
print("average is",average)

higest=0
for k in range(p):
    if k>higest:
        higest=ss(k-1)
        b=ns[k-1]
print("the higest score is",higest,"it is",b)

lowest=100
for u in range(p):
    if u>lowest:
        lowest=ss(u)
        c=ns[u]
print("the lowest score is",lowest,"it is",c)
    
    





