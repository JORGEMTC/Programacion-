# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 07:44:20 2022

@author: Alumno
"""
while(1==1): #Bucle de repeticion  
  print("\n--CALCULADORA DE HORAS--") # Encabezado del Programa
  hora=int(input("Ingrese el valor de las horas[0-23]: ")) # Ingreso de Datos 
  while hora<0 or hora>23: #Bucle de validacion de datos 
    print("El dato de la hora no es correcto") # Mensaje de Error
    hora=int(input("Ingrese el valor de las horas[0-23]: ")) # Nuevo ingreso de datos
  print("\nEl dato es correcto puede continuar") #Fin de Bucle
  minutos=int(input("Ingrese el valor de los minutos [0-59]: ")) # Ingreso de Datos 
  while minutos<0 or minutos>59: #Bucle de validacion de datos 
    print("El dato de los minutos no es correcto")# Mensaje de Error
    minutos=int(input("Ingrese el valor de los minutos [0-59]: "))# Nuevo ingreso de datos
  print("\nEl dato es correcto puede Continuar")#Fin de Bucle
  segundos=int(input("Ingrese el valor de los segundos [0-59]:"))# Ingreso de Datos 
  while segundos<0 or segundos>59: #Bucle de validacion de datos 
    print("\nEl dato de los segundos no es correcto")# Mensaje de Error
    segundos=int(input("Ingrese el valor de los segundos [0-59]:"))# Nuevo ingreso de datos
  print("\n El dato es correcto puede continuar")#Fin de Bucle
  sx=int(input("Porfavor ingrese el valor de los segundos extras:")) # Ingreso de Datos 
  while sx<0: #Bucle de validacion de datos 
    print("\nEl valor de los segundos extras debe ser positivo ")# Mensaje de Error
    sx=int(input("Porfavor ingrese el valor de los segundos extras:"))# Nuevo ingreso de datos
  print("\nPuede Continuar")#Fin de Bucle
  ensegundos=(hora*3600)+(minutos*60)+segundos # Conversion de unidades
  suma=sx+ensegundos # Suma segundos dados
  hh=int(suma/3600) # Conversion de unidades
  mm=int((suma/60)-(hh*60)) # Conversion de unidades
  ss=int((suma-(mm*60)-(hh*3600))) # Conversion de unidades
  if hh<10 and mm>10 and ss>10: # Condicional de impresion horas
    print(f"\nNueva hora:[0{hh}:{mm}:{ss}]") # Impresion Resultado
  if hh>10 and mm<10 and ss>10: # Condicional de impresion horas
    print(f"\nNueva hora:[{hh}:0{mm}:{ss}]") # Impresion Resultado
  if hh>10 and mm>10 and ss<10: # Condicional de impresion horas
    print(f"\nNueva hora:[{hh}:{mm}:0{ss}]") # Impresion Resultado
  if hh<10 and mm<10 and ss>10: # Condicional de impresion horas
    print(f"\nNueva hora:[0{hh}:0{mm}:{ss}]") # Impresion Resultado  
  if hh>10 and mm<10 and ss<10: # Condicional de impresion horas
    print(f"\nNueva hora:[{hh}:0{mm}:0{ss}]") # Impresion Resultado  
  if hh<10 and mm<10 and ss<10: # Condicional de impresion horas
    print(f"\nNueva hora:[0{hh}:0{mm}:0{ss}]") # Impresion Resultado  
  x=input("\nDesea salir digite No caso contrario digite Si: ") # Salir o Continuar en el programa
  if x=="No": #Condicional fin de programa
    break # Interruptor de bucle
