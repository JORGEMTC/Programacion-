# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 18:03:42 2022

@author: Mateo
"""
def validar(nombre,edad,cedula,email):
    t=0
    for t in(nombre):
        if(t.isdigit() ):
          print("No se permiten ingresar numeros en el nombre. \n Entrada:",t)
    y=int(input(edad))
    if y>100 and y<0:
            print("Ingrese una edad valida: ") 
    for i in range(len(cedula)-1):
        x=int(cedula[i])
        if i%2 == 0:
           x=x*2 
           if x>9:
             x=x-9
    suma=0         
    suma = suma+x
    if suma%10 !=0:
       result = 10 - (suma%10)
       if  int(cedula[ -1])== result: 
               print("La cedula {} es ecuatoriana",format(cedula))
       else: 
             print("La cedula {} no es correcta",format(cedula))
  
    import regex
    pattern='^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$'
    userd_id=input (email)
    if regex.search(pattern,userd_id):
       print("Email Valido id") 
    else:
       print("Email Invalido id") 
    return False

print("Los datos son correctos")
print("True")
       
print(validar("Jorge Carrillo","19","175590679","matheocarrillo14@gmail.com"))     


