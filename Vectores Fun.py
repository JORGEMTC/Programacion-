# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 19:04:41 2022

@author: Mateo
"""
from random import randint 
def dimension():
    print("Ingrese la dimension del vector: ")    
dimension()
x= int(input()) 
if x<4 and x>30:
   print("Dimension Fuera de Rango")         
vector=[ ] 
primo=[]
t=0
for i in range(x):
    a=randint(1,100)
    vector.append(a) 
    def numprimos(a,i=2):
        if a%i !=0:
           primo.append(a)
        elif a%i!=0:
             return numprimos(a,i+1)
    numprimos(a)     
    
print("V1: ",vector)
print("Vector Primos=",primo)


    