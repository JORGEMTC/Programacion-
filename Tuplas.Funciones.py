# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 08:02:17 2022

@author: Alumno
"""
def suma(*a):
    print("\nTipo de datos de argumento:",type(a))
    sum=0
    for n in a:
        sum=sum+n
    print("Suma:",sum)

suma(3)
suma(1)
suma(3,5)
suma(4,5,6,7)
suma(1,2,3,4,5,6)
suma(1,2,3,4,5,6,7,8,9,10)
suma(1,2,3,4,5,6,7,8,10,11,12,13,13,14,15,16,17,18,19,20)
    