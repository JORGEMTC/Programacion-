# -*- coding: utf-8 -*-
"""
Created on Fri May 13 07:32:38 2022

@author: Alumno
"""
contador=0
contadorigual=0
contadornegativo=0
while True:
  while True:
      
    x=int(input("Ingrese un 1er numero: "))
    y=int(input("Ingrese un segundo numero:"))
    z=int(input("Si desea terminar el programa digite salir: "))
    
    if x==y:
        print("ERROR los numeros ingresados son iguales")
    elif x<1 and y<1:
        print("Error los numeros ingresados son negativos")
    elif x<1:
        print("ERROR el numero es nagtivo")
    elif y<1:   
        print("ERROR el numero es negativo")   
    else:
        x>=1 and y>=1
        print("Los numeros son correctos")
        
        break
    contador=contador+1
    print("Cuantas veces",contador)
    print("Cuantas veces igual",contadorigual)
    print("Cuantas veces negativo",contadornegativo)
    salir=int(input("Ingresar 0"))
    if salir==0:
          break