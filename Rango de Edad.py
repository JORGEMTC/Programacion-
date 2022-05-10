# -*- coding: utf-8 -*-
"""
Created on Tue May 10 08:04:36 2022

@author: Alumno
"""
edad=int(input("Porfavor ingrese su edad: "))
if edad >=1 and edad <=12:
    print("Usted es un niño")
elif edad>=12 and edad <=19:
     print("Usted es un adolescente:")
elif edad>=19 and edad <=29:
     print("Usted es un joven:")    
elif edad>=30 and edad <=45:
     print("Usted es un adulto:")    
elif edad>=46 and edad <=100:
     print("Usted es un adulto mayor:")           
else:
     print("Segun su edad usted ya se murio")
       

105