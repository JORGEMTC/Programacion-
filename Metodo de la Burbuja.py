# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 21:03:17 2022

@author: Mateo
"""
from random import randint
from time import sleep
x=int(input("Ingrese la dimension del vector: \n"))
vector1=[ ]
for i in range(x):
    a=randint(50,100)
    vector1.append(a)
print("V1: ",vector1)
for i in range (0,x):
    sleep(1)
    print("El vector en posicion",i,"es:",vector1[i])
band=False
while band == False:
    band = True
    for i in range(len(vector1)-1):
        if vector1[i] > vector1[i+1]:
           aux=vector1[i] 
           vector1[i]=vector1[i+1]
           vector1[i+1]=aux
           band = False
print("\nVector Ordenado:",vector1)   
for i in range (0,x):
    sleep(1)        
    print("El vector ordenado en la posición",i,"es:",vector1[i])      