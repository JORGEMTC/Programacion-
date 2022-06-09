# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:53:28 2022

@author: Jorge Carrillo 
 """
num1=1 #Contador
n=int(input("Ingrese el numero de tablas que desea imprimir: ")) #Ingreso de datos
while n<2 or n>100: #Bucle de Repeticion While
       print("Error el numero debe ser mayor a 2 y menor a 100") #Validacion de Datos 
       n=int(input("Ingrese el numero de tablas que desea impimir: ")) #Ingreso de datos 
print("Continuemos") # Mensaje 
while True: #Bucle While True
    m=int(input("Ingrese hasta que numero va ha  multiplicar: ")) #Ingreso de datos
    if m<2: #Validacion de Datos con condicional if
        print("Error el numero debe ser mayor a 2") # Mensaje de Error
    if m>100: #Validacion de Datos con condiocnal if
       print("Error el numero debe ser menor a 100") #Mensaje de Error
    else: #Fin de condional if
        break # Interuptor de Bucle While True 
print("Continuemos") # Mensaje           
while num1<=n: #Bucle de Repeticion While
    print("La tabla de #",num1) #Impresion de Texto 
    num2=1  #Contador
    suma=0  #Contador
    par=0   #Contador
    impar=0 #Contador
    while num2<=m: #Bucle de Repeticion While
        resultado=num2*num1 # Opéracion matematica
        print(num2,"x",num1,"=",resultado) # Impresion tablas de Multiplicar 
        num2+=1 # Operacion Matematica
        if resultado%2==0: # Validacion de Numeros Pares Condicional if  
            par+=1 #Contador de Numeros Pares
        else: # Validacion de Numeros Impares
            impar+ 1 # Comtador de numeros Impares
        suma+=resultado # Suma  de los resultados 
    num1+=1 # Contador de Resultados 
    print("La suma de los valores es:",suma) # Impresion suma
    print("El promedio es:",suma//m) # Impresion Promedio
    print("Hay",par,"numeros pares") # Impresion numeros Pares
    print("Hay",impar,"numeros impares","\n") # Impresion numeros Impares

