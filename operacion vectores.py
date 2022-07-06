# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 07:10:09 2022

@author: Mateo
"""
while (1==1):
    from random import randint
    x=int(input("Ingrese la dimension del vector: "))
    if x>5 and x<30:
        vector1=[ ]
        for i in range(x):
            a=randint(0,100)
            vector1.append(a)
            print("V1: ",vector1)
    
        vector2=[ ]
        for i in range(x):
            b=randint(0,100)
            vector2.append(b)
            print("V2: ",vector2)
        
        vector3=[0]*x
    
        O=input("Que operacion matematica desea realizar: ")
        if O=="suma":
            for i in range(x):
                vector3[i]=vector1[i]+vector2[i]
            for i in range(x):
                print(vector3[i],end=" ")   
    
        if O=="resta":
           for i in range(x):
               vector3[i]=vector1[i]-vector2[i]
           for i in range(x):
               print(vector3[i],end=" ")   
    
        if O=="multiplicacion":
            for i in range(x):
                vector3[i]=vector1[i]*vector2[i]
            for i in range(x):
                print(vector3[i],end=" ")   
    
        if O=="division":
            for i in range(x):
                vector3[i]=vector1[i]/vector2[i]
            for i in range(x):
                print(vector3[i],end=" ")   
   
    else:
         print("La dimension deben ser mayor a 5 y menor a 30")
     
    x=input("\nDesea salir digite No caso contrario digite Si: ")    
    if x=="No":    
       break