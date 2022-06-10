# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 22:07:27 2021

@author: Juan Carlos

"""
def keyw(**datos):
    print("\nTipo de datos del argumento:",type(datos))

    for key, value in datos.items():
        print("{} es {}".format(key,value))

keyw(Nombre="Juan", 
     Apellido="Domínguez", 
     Edad=42, 
     Telefono=1234567890)
keyw(Nombre="John", 
     Apellido="Wood",
     Email="johnwood@nomail.com",
     Pais="Wakanda", 
     Edad=25, 
     Telefono=9876543210)