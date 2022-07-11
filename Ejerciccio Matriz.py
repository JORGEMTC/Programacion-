# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 11:24:06 2022

@author: Mateo
"""
from random import randint
x=int(input("Ingrese el numero de filas:"))
y=int(input("Ingrese el numero de columnas:"))
while x<4 or y<4:
    print("Error, los valores deben ser mayores que 4")
    x=int(input("Ingrese el numero de filas:"))
    y=int(input("Ingrese el numero de columnas:"))
print("El valor es correcto")     
while x>30 or y>30:
    print("Error los numeros deben ser menores a 30")
    x=int(input("Ingrese el numero de filas:"))
    y=int(input("Ingrese el numero de columnas:")) 
print("El valor es correcto")        
matriz=[[int()for i in range (x)]for j in range(y)]

for filas in range(x):
    for columnas in range(y):
        matriz[filas][columnas]=randint(0,100)
for filas in range (x):
    for columnas in range(y):
         print("|",matriz[filas][columnas],end=(""))
    print("\n")
    PromFilas  =(columnas+filas)/x
    promColumnas  =(columnas+filas)/y
    PromedioT=PromFilas+promColumnas
print("El promedio Total de la matriz es: ", PromedioT)

Ma=matriz[0][0]
Me=matriz[0][0]
for fila in matriz:
    for x in fila:
        if x > Ma:
           Ma = x 
print("El valor mas alto es",Ma,",y es se ubica en",fila)           
          