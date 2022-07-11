# -*- coding: utf-8 -*-
"""
Created on Mon May 16 18:20:49 2022

@author: Mateo
"""
from math import sqrt

def a():
    print("a: ")
    return a
def b():
    print("b: ")
    return b
def c():
    print("c:")
    return c
    
a()   
a=float(input())
b()
b=float(input())
c()
c=float(input())    
x1=0 
x2=0

E=(b**2)-(4*(a)*(c))
if E<0:
   print("Division para cero o Raiz Negativa") 
else:   
    x1= (-b+sqrt(E)) / (2*a)
    if E!= 0:
       x2= (-b-sqrt(E)) / (2*a)
    else:
        print("Respuestas")
    print("x1= ",x1)
    print("x2= ",x2)