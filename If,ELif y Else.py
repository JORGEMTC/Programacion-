# -*- coding: utf-8 -*-
"""
Created on Tue May 10 07:57:45 2022

@author: Alumno
"""

acl=int(input("Ingrese el # de ACL: "))
if acl>=1 and acl<=99:
    print("Es un ACL Estandar")
elif acl>=100 and acl <=199:
    print("Es un ACL Extendida")
else:
    print("El # Ingresado no es de un ACL")
    