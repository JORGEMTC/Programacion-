# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 08:43:04 2022

@author: Mateo
"""
from random import randint
matrix = [[int() for i in range(4)] for j in range(4)]
for filas in range(4):
    for columnas in range(4):
        a=randint(0,100)
        matrix[filas][columnas]=a
for i in range(4):
    print("| ",end="")
    for j in range(4):
        print(matrix[i][j]," | ",end="")        
    print("\n")    