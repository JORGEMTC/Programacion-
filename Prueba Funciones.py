# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 07:46:39 2022

@author: Alumno
"""
def ordena(lst=[]):
    print("Lista:",lst)
    s=[lst]
    for i in range(len(lst)-1): # Recorre la lista en indica el numero de elemnetos que tiene la lista
        for m in range(len(lst)-1): #Desplaza los elementos a izquierda
            if lst[m]>lst[m+1]:
                time=lst[m] #Almacena un dato durante la comparacion 
                lst[m]=lst[m+1]
                lst[m+1]=time
    print("Lista Ordenada:",s)                    
ordena(lst=[50,30,200,52,34,1001,5]) 
