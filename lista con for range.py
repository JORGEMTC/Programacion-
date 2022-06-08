# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 11:52:52 2022

@author: lab
"""
lista=[]
suma=0
for i in range (1,11):
    valor=int(input("Ingrese las estaturas: "))
    lista.append(valor)
    suma=suma+valor
    promedio=suma/10
print("La lista es:lista",lista) 
print("La suma es: ",suma)
print("El promedio es: ",promedio)    
