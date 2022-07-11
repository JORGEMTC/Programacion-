# -*- coding: utf-8 -*-
"""
Created on Mon May 16 18:24:19 2022

@author: Mateo
"""
a=int(input("Ingrese el valor de a:"))
b=int(input("Ingrese el valor de b:"))
c=int(input("Ingrese el valor de c:"))
import math
d=(b**2)-4*a*c
y=math.sqrt(d)
resultado1=-b+d/2*a
print(f"Resultado 1: {resultado1}")
resultado2=-b-d/2*a
print(f"Resultado 2: {resultado2}")