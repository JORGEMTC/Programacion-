# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 07:44:52 2022

@author: Mateo
"""
import math 
   
def rev(num): 
    return int(num != 0) and ((num % 10)*(10**int(math.log(num, 10)))+ rev(num // 10)) 
  
test_number = 525
  
print ("Numero es: " + str(test_number)) 
  
res = test_number == rev(test_number) 
  
print ("El numero",test_number," es palindromo ? : " + str(res)) 
