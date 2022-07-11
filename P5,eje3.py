# -*- coding: utf-8 -*-
"""
Created on Mon May 16 17:15:17 2022

@author: Mateo
"""
telefono=int(input("Ingrese el numero de telefono(9 numeros sin el 0):"))
hora=int(input("Ingrese la hora[0-23]:"))
minutos=int(input("Ingrese los minutos[0-59]:998927674 "))
if hora>=00 and hora<=8 and minutos>=20:
  print("Si contestar")
elif hora>= 8 and minutos>= 20 and hora<=13:
  print("No Contestar")
elif hora>= 8 and minutos>= 20 and hora<=13 and telefono==909:
  print("Si Contestar")  
elif hora>=13 and hora <=19 and minutos<=50:
   print("Si contestar")
elif hora>= 13 and minutos>= 19 and hora<=50 and telefono==877:
  print("No Contestar")   
else:
   hora>=19 and minutos >=50 and hora<=23
   print("No contestar")
 