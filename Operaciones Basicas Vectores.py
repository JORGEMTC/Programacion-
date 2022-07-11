# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 07:10:08 2022

@author: Mateo
"""

vector1=[1,2,3,4,5,6,7,8,9,10]
vector2=[1,2,3,4,5,6,7,8,9,10]
vector3=[0]*10
for i in range(10):
    vector3[i]=vector1[i]/vector2[i]
for i in range(10):
    print(vector3[i],end=" ")

print("")
print(vector3)    