# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 12:24:16 2022

@author: Mateo
"""
def N():
    print("n:")
    return N
N()
a=int(input())
if a<0:
    print("El valor de N debe ser positivo")
else:
    suma=0
    x=1
    for a in range (a):
        r=2**x
        x+=1
        suma=suma+r
    print("\nResultado:",suma) 
    