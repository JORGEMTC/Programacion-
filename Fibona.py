# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 21:52:06 2022

@author: Mateo
"""

from math import sqrt # Importacion de libreria math para realizar la raiz cuadrada
def N(a): # Definicion de una funcion N
    return ((1+sqrt(5))**a-(1-sqrt(5))**a)/(2**a*sqrt(5)) # Operacion Matematica
def Fib(inicio,fin): # Definicion de variable Fib
    a = 0 # Acumulador
    d=N(a) # Variable
    while d <= fin: # Bucle de Repeticion
        if inicio <= d: # Validacion de Datos
           print(d) # Impresion seria 
        a+=1  # Contador
        d=N(a) # Variable
          
Fib(0,100) # Invocacion de Funcion Fib   