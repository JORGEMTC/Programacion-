# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 13:58:28 2022

@author: lab
"""
for n in range (1,16): # Bucle con rango definido
  print(f"La tabla de # {n}") #Impresion de texto
  suma=0 #Acumuladores
  par=0 #Acumuladores
  impar=0 #Acumuladores
  for i in range (1,16): # Bucle con rango definido
    m=i*n # Operacion matematica
    print(i,"x",n,"=",m) #Impresion Tablas de Multuplicar
    if m%2==0: #Validacion de numeros parees
      par=par+1 #Contador de numeros pares
    else: #Validacion de nuermos impares
      impar=impar+1 # Contador de nuemros impares
    suma=suma+m #operacion matematica 
  promedio=suma//15 #Promedio Resultados
  print(f"La suma de los valores es: {suma}") # Impresion suma
  print(f"El promedio es: {promedio}") # Impresion Promedio
  print(f"Hay {par} numeros pares") # Impresion numeros Pares
  print(f"Hay {impar} numeros impares") # Impresion numeros Impares
