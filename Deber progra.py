# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 21:13:54 2022

@author: Mateo
"""
def añobisiesto(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
 
def diasmes(year, month):
    diasMeses = [31,28,31,30,31,30,31,31,30,31,30,31]
    if añobisiesto(year):
        if diasMeses[month - 1] == 28:
            return 29
        else:
            return diasMeses[month - 1]
    else:
        return diasMeses[month - 1]
    return None
 
testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
 
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end="")
	result = diasmes(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Error")