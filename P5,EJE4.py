# -*- coding: utf-8 -*-
"""
Created on Mon May 16 16:54:17 2022

@author: Mateo
"""
pasajero=input("Ingrese el nombre del pasajero: ")
pasaje=int(input("Ingrese el valor del pasaje: "))
edad=int(input("Ingrese la edad: "))
nacionalidad=input("Ingrese la nacionalidad: ")
descuento=pasaje*0.40
total=pasaje-descuento
if edad <12 and nacionalidad=="ecuatoriano:
  print(f"El descuento aplicado es de: {descuento}")
  print(f"El total a pagar por {pasajero} es:{total}")
elif edad==12 and nacionalidad=="ecuatoriano":
     print(f"El descuento aplicado es de: {descuento}")
     print(f"El total a pagar por {pasajero} es:{total}")  
elif edad>12 and edad<65 and nacionalidad=="ecuatoriano":
     print(f"El pasajero {pasajero} no tiene descuento por su rango de edad {edad}")   
else:
      edad >65 and nacionalidad=="ecuatoriano" 
      print(f"El descuento aplicado es de: {descuento}")
      print(f"El total a pagar por {pasajero} es:{total}")  
                                              
