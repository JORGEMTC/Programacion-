# -*- coding: utf-8 -*-
"""
Created on Fri May 13 07:19:09 2022

@author: Alumno
"""

while True:
    x=input("Enter a numbern to count to:")
    if x=='q' or x=='quit':
       break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
break