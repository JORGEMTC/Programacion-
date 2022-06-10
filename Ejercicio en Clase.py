# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 08:21:57 2022

@author: Alumno
"""
def factor(n):
    n=int(input("Ingrese un numero: "))
    while  n<2 or n>100:
        print("El numero ingresado debe ser mayor a 2 y menor que 100")
        n=int(input("Ingrese un numero: "))
        print("Continuar") 
    factores=[]
        

   