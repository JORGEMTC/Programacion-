# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:35:09 2022

@author: Mateo
"""
fosforos=int(input("Ingrese la cantidad de fosforos que tiene en stock: "))
caja=fosforos//40
sobrante=(caja*40)
paquete=caja//12
sobra=caja-(12*paquete)

print(f"Con {fosforos}  fosforos se puede llenar {caja} cajas ")
print("La cantidad de fosoforos que sobran es:")
print(fosforos-int(caja)*40)
print(f"Se produjo {paquete} paquetes")
print(f"Sobran {sobra} cajas")
