# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 15:51:56 2022

@author: Mateo
"""
def bisiesto(año,mes):
    if año%4==0:
       print("El año tiene 366 dias ")
    if mes==2 and año%4==0:
        print("El mes tiene 29 dias ")
    if mes==4 and 6 and 9 and 11:
        print("El mes tiene 30 dias")
    if mes== 1 and 3 and 5 and 7 and 8 and 10 and 12:
        print("El mes tiene 31 dias")   
    if año%4!=0:   
        print("El año tiene 365 dias ")
    if mes==2 and año%4!=0 :
         print("El mes tiene 28 dias ")
    if mes==4 and 6 and 9 and 11 and año%4!=0:
         print("El mes tiene 30 dias")  
    if mes== 1 and 3 and 5 and 7 and 8 and 10 and 12 and año%4!=0:
         print("El mes tiene 31 dias ")
    return     
bisiesto(2012,2)        
    
    
    
    
