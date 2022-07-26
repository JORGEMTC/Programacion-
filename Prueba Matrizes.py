# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 22:07:11 2022

@author: Jorge Matheo :)
"""

import random
from pandas import pd


while (1==1):
    
  filas = int(input("Ingrese el numero de materias que va a tener su sistema de calificaciones:"))
  while filas < 1 or filas > 10:
    print('Error, la cantidad de materias debe estar entre 1 y 10!')
    filas = int(input("Ingrese el numero de materias que va a tener su sistema de calificaciones:"))

  columnas = int(input("Ingrese el numero de notas que van a tener las materias:"))
  while columnas < 1 or columnas > 7:
    print('Error, las notas debe estar entre 1 y 10!')
    columnas = int(input("Ingrese el numero de notas que van a tener las materias:"))


  matriz = []
  materias = []


  for i in range(filas):
    materias.append(input("Ingrese la materia:",{i+1}))

  for i in range(filas):
    notas = []
    for j in range(columnas):
      nota = random.randint(0,10)
      notas.append(nota)
  
    matriz.append(notas)

  df = pd.DataFrame(index=materias, data=matriz, columns=[f'Nota {i}' for i in range(1, columnas+1)])
  print(df)
  
  opcion = 0
  while opcion < 0 or opcion > filas:
    for i in range(filas):
      print(f'[{i+1}] {materias[i]}')
    opcion = int(input('Ingrese el numero de materia para realizar el reporte: '))

  
  promedioMateria = sum(matriz[opcion]) / columnas
  promedioMateria = round(promedioMateria, 2)
  print("Promedio de la meteria de",materias[opcion]," es:",promedioMateria)


  notaMinima = matriz[opcion][0]
  notaMaxima = matriz[opcion][0]

  for j in range(columnas):
    if notaMinima > matriz[opcion][j]:
      notaMinima = matriz[opcion][j]
    if notaMaxima < matriz[opcion][j]:
      notaMaxima = matriz[opcion][j]
  
  print("La nota mínima es: ",notaMinima)
  print("La nota maxima es:",notaMaxima)


  suma = 0
  for i in range(filas):
    s = 0
    for j in range(columnas):
      s += matriz[i][j]
    suma += s / columnas
  
  promedio = round(suma/filas, 2)

  if promedio > promedioMateria:
    print("El promedio de la materia es",promedioMateria,"y es menor a la media general de calificaciones",promedio)
  else:
    print("El promedio de la materia",promedioMateria,"y es superior a la media general de calificaciones",promedio)
  
    
  s = input("Si desea salir digite Si, caso contrario No: \n")
  if s=="Si":
      break 
   