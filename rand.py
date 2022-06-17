# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 17:57:52 2022

@author: Mateo
"""
def RND(n): #Definicion de Funcion RND
    import random # Imporatcion de Libreria Ramdom
    lista = [ ] # Lista 
    for i in range(n): # Bucle con rango definido
        a=random.randint(0, 1000) # Genrador de nuemros Randomianos
        lista.append(a) #Almacenamiento de datos en lista
    print(lista) # Impresion Lista
    
RND(2) # Invocacion de Variable RND