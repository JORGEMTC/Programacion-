# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 07:45:42 2022

@author: Alumno
"""
count =0;
numero=int(input("Ingrese un número(debe ser mayor que 1):"))
while numero<=1:
    print("Error debe ingresar un número mayor que 1")
    break;
while numero>1:
    print("Puede continuar")
    break;
while numero ==2:
    print("El 2 es el primer numero primo")
    break;
aux=0;
promedio=0;
aux2=0
for n in range(1,numero+1):
    for d in range(1,n+1):
        if n % d == 0:
            count+=1;
    if count == 2:
        aux+=n;
        aux2+=1;
        print("{}".format(n),end=" ")
    count =0
print("\nSuma de todos los elementos: ");
print(aux)
print("Promedio de todos los numeros primeros hasta N")
promedio=aux/aux2
print(promedio)
