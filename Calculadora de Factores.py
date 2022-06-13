# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13 16:05:59 2022

@author: Mateo
"""
def divisores(): # Definicion de la funcion.
  n=int(input("Ingrese un numero: ")) # Ingreso de datos.
  if n<2 and n>100: # Validacion de datos.
    print("El numero debe ser mayor a 2 y menor a 100") # Mensaje de Error.
  fac =[] # Declaracion de Lista.
  i=1 # Acumulador.
   
  while i <=n: # Bucle de repeticion.
   if n % i ==0: # Validacion de factores.
    fac.append(n//i) # Adjunto de Datos a la Lista.
    fac.sort() # Funcion de Clasificacion .
   i=i+1 # Contador.
  print("Los factores del numero", n, "son: ") # Mensaje de resultado.
  for f in fac: # Bucle for.
    print(f, end=",") # Impresion de resultado.
divisores() # Impresion de Resultados.
