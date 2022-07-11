# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 07:25:45 2022

@author: Mateo
"""
def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    return True
es_primo(7)