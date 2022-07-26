# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 20:18:36 2022

@author: Mateo
"""
import random
while True:
    x=int(input("Ingrese el numero de filas: "))
    if x<4 or x>10:
        print("Error el valor no puede ser menor a 4 o mayor a 10")
    else:
        break
while True:
    y=int(input("Ingrese el numero de columnas: "))
    if y<4 or y>10:
        print("Error el valor no puede ser menor a 4 o mayor a 10")
    else:
        break
    
matriz = [[int() for i in range(y)] for j in range(x)]

def numrandom():
    for f in range(x):
        for c in range(y):
            valor=random.randint(0,5)
            matriz[f][c]=valor
        
numrandom()

for i in range(x):
    print("|", end=" ")
    for j in range(y):
        print(matriz[i][j],"|",end=" ")
    print("\n")

def sumaf(x):
    sumaf=0
    for s in range(y):
        valorf=matriz[x-1][s]
        sumaf+=valorf
    print("la suma de la fila",x,"es:",sumaf)
    
def sumac(y):
    sumac=0
    for b in range(x):
        valorc=matriz[b][y-1]
        sumac+=valorc
    print("la suma de la columna",y,"es:",sumac)
    print("\n")

for k in range(x):   
    sumaf(k+1)
    sumac(k+1)

def promedio():
    sumat=0
    for p in range(x):
        for q in range(y):
            suma=matriz[p][q]
            sumat+=suma
    print("El promedio de los numeros de la matriz es:",sumat/(x*y))
promedio()
