# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 20:33:29 2022

@author: Mateo
"""

print("********** Proyecto Integrador **********")
print("****** Tabla Periodica Elementos mas Usados ******")
    
def mostrar_menu(opciones):
    print('Seleccione la clase de elemento que desea buscar:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, selecione una de las opcionnes senaladas.')
    return a

def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
          mostrar_menu(opciones)
          opcion = leer_opcion(opciones)
          ejecutar_opcion(opcion, opciones)
          print()
    while opcion ==opcion_salida :
          break
    
def menu_principal():
    opciones = {
    "1": ("Alcalinos", accion1),
    "2": ("Alcalinoterreos", accion2),
    "3": ("Metales de Transicion", accion3),
    "4": ("No Metales",accion4),
    "5": ("Halogenos",accion5),
    "6": ("Gases Nobles",accion6),
    "7": ("Salir del Programa", salir)
    }
    generar_menu(opciones,"7")

#Alcalinos

def accion1():
    def mostrar_menu(opciones):
        print('Seleccione el tipo de elemento que desea buscar:')
        for clave in sorted(opciones):
            print(f' {clave}) {opciones[clave][0]}')

    def leer_opcion(opciones):
        while (a := input('Opción: ')) not in opciones:
            print('Opción incorrecta, selecione una de las opcionnes senaladas.')
        return a

    def ejecutar_opcion(opcion, opciones):
        opciones[opcion][1]()

    def generar_menu(opciones, opcion_menu_principal):
        opcion = None
        while opcion != opcion_menu_principal:
              mostrar_menu(opciones)
              opcion = leer_opcion(opciones)
              ejecutar_opcion(opcion, opciones)
              print()

    def menu_secundario():
        opciones = {
        "1": ("Litio [Li]", accion1),
        "2": ("Sodio [Na]", accion2),
        "3": ("Potasio [K]", accion3),
        "4": ("Rubidio [Rb]",accion4),
        "5": ("Cesio [Cs]",accion5),
        "6": ("Francio [Fr]",accion6),
        "7": ("Retorno Menu Principal", menu_principal)
        }
        generar_menu(opciones,"7")
    def accion1():
        print("Litio [Li]")
        print("Numero de Electrones: 3 ")
        print("Numero de Oxidacion: +1 ")
        print("Masa Atomica: 6.941 umas")
        print("Configuracion Electronica:[1s1 2s2]")
        
    def accion2():
        print("Sodio [Na]")
        print("Numero de Electrones: 11 ")
        print("Numero de Oxidacion: +1 ")
        print("Masa Atomica: 22.98976928 umas")
        print("Configuracion Electronica:[1s1 2s2 2p6 3s1]")
        
    def accion3():
        print("Potasio [K]")
        print("Numero de Electrones: 19 ")
        print("Numero de Oxidacion: +1 ")
        print("Masa Atomica: 39.0983 umas")
        print("Configuracion Electronica:[1s1 2s2 2p6 3s2 3p6 4s1]")
        
    def accion4():
        print("Rubidio [Rb]")
        print("Numero de Electrones: 37 ")
        print("Numero de Oxidacion: +1 ") 
        print("Masa Atomica: 85.4678 umas")
        print("Configuracion Electronica:[[Kr]5s1]")
        
    def accion5():
        print("Cesio [Cs]")
        print("Numero de Electrones: 55 ")
        print("Numero de Oxidacion: +1 ")
        print("Masa Atomica: 132.9054519 umas")
        print("Configuracion Electronica:[[Xe] 6s1]")
        
    def accion6():
        print("Francio [Fr]")
        print("Numero de Electrones: 7 ")
        print("Numero de Oxidacion: +1 ")
        print("Masa Atomica: 223 umas")
        print("Configuracion Electronica:[[Rn] 7s1]") 
    if __name__ == '__main__':
        menu_secundario()
 
    
# Alcalinoterreos
def accion2():
    
    def mostrar_menu(opciones):
        print('Seleccione el tipo de elemento que desea buscar:')
        for clave in sorted(opciones):
            print(f' {clave}) {opciones[clave][0]}')

    def leer_opcion(opciones):
        while (a := input('Opción: ')) not in opciones:
            print('Opción incorrecta, selecione una de las opcionnes senaladas.')
        return a

    def ejecutar_opcion(opcion, opciones):
        opciones[opcion][1]()

    def generar_menu(opciones, opcion_menu_principal):
        opcion = None
        while opcion != opcion_menu_principal:
              mostrar_menu(opciones)
              opcion = leer_opcion(opciones)
              ejecutar_opcion(opcion, opciones)
              print()

    def menu_secundario2():
        opciones = {
        "1": ("Berilio [Be]", accion1),
        "2": ("Magnesio [Mg]", accion2),
        "3": ("Calcio [Ca]", accion3),
        "4": ("Estroncio [Sr]",accion4),
        "5": ("Bario [Ba]",accion5),
        "6": ("Radio [Ra]",accion6),
        "7": ("Retorno Menu Principal", menu_principal)
        }
        generar_menu(opciones,"7")
    def accion1():
        print("Berilio [Be]")
        print("Numero de Electrones: 4 ")
        print("Numero de Oxidacion: +2 ")
        print("Masa Atomica: 9.012182 umas")
        print("Configuracion Electronica:[[He] 2s²]")
        
    def accion2():
        print("Magnesio [Mg]")
        print("Numero de Electrones: 12 ")
        print("Numero de Oxidacion: +2 ")
        print("Masa Atomica: 24.305 umas")
        print("Configuracion Electronica:[[Ne] 3s²]")
        
    def accion3():
        print("Calcio [Ca]")
        print("Numero de Electrones: 20 ")
        print("Numero de Oxidacion: +2 ")
        print("Masa Atomica: 40.078 umas")
        print("Configuracion Electronica:[[Ar] 4s²]")
        
    def accion4():
        print("Estroncio [Sr]")
        print("Numero de Electrones: 38 ")
        print("Numero de Oxidacion: +2 ") 
        print("Masa Atomica: 87.62 umas")
        print("Configuracion Electronica:[[Kr]5s2]")
        
    def accion5():
        print("Bario [Ba]")
        print("Numero de Electrones: 56 ")
        print("Numero de Oxidacion: +2 ")
        print("Masa Atomica: 137.327 umas")
        print("Configuracion Electronica:[[Xe] 6s2]")
        
    def accion6():
        print("Radio [Ra]")
        print("Numero de Electrones: 8 ")
        print("Numero de Oxidacion: +2 ")
        print("Masa Atomica: 226 umas")
        print("Configuracion Electronica:[[Rn] 7s2]") 
    if __name__ == '__main__':
        menu_secundario2()
    
#Metales de Transicion     
def accion3():
    def mostrar_menu(opciones):
        print('Seleccione el tipo de elemento que desea buscar:')
        for clave in sorted(opciones):
            print(f' {clave}) {opciones[clave][0]}')

    def leer_opcion(opciones):
        while (a := input('Opción: ')) not in opciones:
            print('Opción incorrecta, selecione una de las opcionnes senaladas.')
        return a

    def ejecutar_opcion(opcion, opciones):
        opciones[opcion][1]()

    def generar_menu(opciones, opcion_menu_principal):
        opcion = None
        while opcion != opcion_menu_principal:
              mostrar_menu(opciones)
              opcion = leer_opcion(opciones)
              ejecutar_opcion(opcion, opciones)
              print()

    def menu_secundario3():
        opciones = {
        "1": ("Cromo [Cr]", accion1),
        "2": ("Manganeso [Mn]", accion2),
        "3": ("Hierro [Fe]", accion3),
        "4": ("Cobalto [Co]",accion4),
        "5": ("Niquel [Ni]",accion5),
        "6": ("Cobre [Cu]",accion6),
        "7": ("Zinc [Zn]",accion7),
        "8": ("Plata [Ag]",accion8),
        "9": ("Cadmio [Cd]",accion9),
        "10":("Paladio [Pd]",accion10),
        "11":("Oro [Au]",accion11),
        "12":("Mercurio [Hg]",accion12),
        "13":("Platino [Pt]",accion13),
        "14":("Aluminio [Al]",accion14),
        "15":("Galio [Gl]",accion15),
        "16":("Indio [In]",accion16),
        "17":("Estaño [Sn]",accion17),
        "18":("Talio [Tl]",accion18),
        "19":("Plomo [Pb]",accion19),
        "20":("Bismuto [Bi]",accion20),
        "21": ("Retorno Menu Principal", menu_principal)
        }
        generar_menu(opciones,"21")
    def accion1():
        print("Cromo [Cr]")
        print("Numero de Electrones: 24 ")
        print("Numero de Oxidacion: +2,+3,+6 ")
        print("Masa Atomica: 51.9961 umas")
        print("Configuracion Electronica:[[Ar] 3d⁵ 4s¹ ]")
        
    def accion2():
        print("Manganeso [Mn]")
        print("Numero de Electrones: 54 ")
        print("Numero de Oxidacion: +2,+3,+4,+6,+7")
        print("Masa Atomica:54.93804  umas")
        print("Configuracion Electronica:[[Ar] 3d5 4s2]")
        
    def accion3():
        print("Hierro [Fe]")
        print("Numero de Electrones: 26 ")
        print("Numero de Oxidacion: +2,+3")
        print("Masa Atomica:55.845 umas")
        print("Configuracion Electronica:[ [Ar] 3d6 4s2]")
        
    def accion4():
        print("Cobalto [Co]")
        print("Numero de Electrones: 27 ")
        print("Numero de Oxidacion: +2 ") 
        print("Masa Atomica:58.933195  umas")
        print("Configuracion Electronica:[[Ar] 3d⁷4s²]")
        
    def accion5():
        print("Niquel [Ni]")
        print("Numero de Electrones: 28 ")
        print("Numero de Oxidacion: +2 ")
        print("Masa Atomica:58.6934 umas")
        print("Configuracion Electronica:[[Ar] 3d⁸4s²]")
        
    def accion6():
        print("Cobre [Cu]")
        print("Numero de Electrones: 29 ")
        print("Numero de Oxidacion: +1,+2")
        print("Masa Atomica:63.546  umas")
        print("Configuracion Electronica:[[Ar] 3d¹⁰ 4s¹]")
     
    def accion7():
        print("Zinc [Zn]")
        print("Numero de Electrones: 30 ")
        print("Numero de Oxidacion: +2 ")
        print("Masa Atomica: 65.38 umas")
        print("Configuracion Electronica:[[Ar] 3d¹⁰ 4s²]")
        
    def accion8():
        print("Plata [Ag]")
        print("Numero de Electrones: 47 ")
        print("Numero de Oxidacion: +1 ")
        print("Masa Atomica: 107.8682 umas")
        print("Configuracion Electronica:[[Kr] 4d¹⁰ 5s¹]")
        
    def accion9():
        print("Cadmio [Cd]")
        print("Numero de Electrones: 48 ")
        print("Numero de Oxidacion: +1,+2 ")
        print("Masa Atomica: 112.411 umas")
        print("Configuracion Electronica:[ [Kr] 4d¹⁰5s²]")
        
    def accion10():
        print("Paladio [Pd]")
        print("Numero de Electrones: 46 ")
        print("Numero de Oxidacion: +1,+2 ")
        print("Masa Atomica:106.42  umas")
        print("Configuracion Electronica:[[Kr] 4d¹⁰]")
        
    def accion11():
        print("Oro [Au]")
        print("Numero de Electrones: 79 ")
        print("Numero de Oxidacion: +1,+3 ")
        print("Masa Atomica: 196.966569 umas")
        print("Configuracion Electronica:[[Xe] 4f14 5d10 6s1]")
        
    def accion12():
        print("Mercurio [Hg]")
        print("Numero de Electrones: 80 ")
        print("Numero de Oxidacion: +1,+2 ")
        print("Masa Atomica:200.59 umas")
        print("Configuracion Electronica:[ [Xe] 4f14 5d10 6s2]")
        
    def accion13():
        print("Platino [Pt]")
        print("Numero de Electrones: 78 ")
        print("Numero de Oxidacion: +2,+4 ")
        print("Masa Atomica: 195.084 umas")
        print("Configuracion Electronica:[[Xe]4f¹⁴5d⁹6s¹]")
     
    def accion14():
        print("Aluminio [Al]")
        print("Numero de Electrones: 13 ")
        print("Numero de Oxidacion: +3")
        print("Masa Atomica:26.981539 umas")
        print("Configuracion Electronica:[[Ne] 3s² 3p¹]")
         
    def accion15():
        print("Galio [Ga]")
        print("Numero de Electrones: 31")
        print("Numero de Oxidacion: +3")
        print("Masa Atomica:69.723 umas")
        print("Configuracion Electronica:[[Ar]3d10 4s2 4p1]") 
        
    def accion16():
        print("Indio [In]")
        print("Numero de Electrones: 49 ")
        print("Numero de Oxidacion: +3 ")
        print("Masa Atomica: 114.818 umas")
        print("Configuracion Electronica:[[Kr]4d10 5s2 5p1]") 
        
    def accion17():
        print("Estano [Sn]")
        print("Numero de Electrones: 50 ")
        print("Numero de Oxidacion: +2,+4 ")
        print("Masa Atomica: 118.71 umas")
        print("Configuracion Electronica:[[Kr]4d¹⁰5s²5p²]")    
       
    def accion18():
        print("Talio [Tl]")
        print("Numero de Electrones: 81 ")
        print("Numero de Oxidacion: +3 ")
        print("Masa Atomica: 204.3833 umas")
        print("Configuracion Electronica:[[Xe]4f14 5d10 6s2 6p1]")
        
    def accion19():
        print("Plomo [Pb]")
        print("Numero de Electrones: 82 ")
        print("Numero de Oxidacion: +2,+4 ")
        print("Masa Atomica:207.2 umas")
        print("Configuracion Electronica:[[Xe]6s² 4f¹⁴ 5d¹⁰ 6p²]")    
        
    def accion20():
        print("Bismuto [Bi]")
        print("Numero de Electrones: 83 ")
        print("Numero de Oxidacion: +3,+5 ")
        print("Masa Atomica: 208.9804 umas")
        print("Configuracion Electronica:[[Xe]4f14 5d10 6s2 6p3]")  
    
    if __name__ == '__main__':
        menu_secundario3()

#No Metales        
def accion4():
    def mostrar_menu(opciones):
        print('Seleccione el tipo de elemento que desea buscar:')
        for clave in sorted(opciones):
            print(f' {clave}) {opciones[clave][0]}')

    def leer_opcion(opciones):
        while (a := input('Opción: ')) not in opciones:
            print('Opción incorrecta, selecione una de las opcionnes senaladas.')
        return a

    def ejecutar_opcion(opcion, opciones):
        opciones[opcion][1]()

    def generar_menu(opciones, opcion_menu_principal):
        opcion = None
        while opcion != opcion_menu_principal:
              mostrar_menu(opciones)
              opcion = leer_opcion(opciones)
              ejecutar_opcion(opcion, opciones)
              print()

    def menu_secundario4():
        opciones = {
        "1": ("Hidrogeno [H]", accion1),
        "2": ("Carbon [C]", accion2),
        "3": ("Nitrogeno [N]", accion3),
        "4": ("Fosforo [P]",accion4),
        "5": ("Oxigeno [O]",accion5),
        "6": ("Azufre [S]",accion6),
        "7": ("Selenio [Se]",accion7),
        "8": ("Retorno Menu Principal", menu_principal)
        }
        generar_menu(opciones,"8")
    def accion1():
        print("Hidrogeno [H]")
        print("Numero de Electrones: 1 ")
        print("Numero de Oxidacion: +1 ")
        print("Masa Atomica: 1 uma")
        print("Configuracion Electronica:[1s1]")
        
    def accion2():
        print("Carbon [C]")
        print("Numero de Electrones: 12 ")
        print("Numero de Oxidacion: +2,+4")
        print("Masa Atomica: 12 umas")
        print("Configuracion Electronica:[[He] 2s2 2p2]")
        
    def accion3():
        print("Nitrogeno [N]")
        print("Numero de Electrones: 7 ")
        print("Numero de Oxidacion: -3,+3,+5 ")
        print("Masa Atomica: 14.0067 umas")
        print("Configuracion Electronica:[[He] 2s2 2p3]")
        
    def accion4():
        print("Fosforo [P]")
        print("Numero de Electrones: 15 ")
        print("Numero de Oxidacion: -1,+1,+3,+5") 
        print("Masa Atomica: 30.973762 umas")
        print("Configuracion Electronica:[[Ne] 3s² 3p³]")
        
    def accion5():
        print("Oxigeno [O]")
        print("Numero de Electrones: 8 ")
        print("Numero de Oxidacion: -2 ")
        print("Masa Atomica: 16 umas")
        print("Configuracion Electronica:[[He] 2s²2p⁴]")
        
    def accion6():
        print("Azufre [S]")
        print("Numero de Electrones: 16 ")
        print("Numero de Oxidacion: +2,+4.+6 ")
        print("Masa Atomica: 32 umas")
        print("Configuracion Electronica:[[Ne] 3s²3p⁴]") 
        
    def accion7():
        print("Selenio [Se]")
        print("Numero de Electrones: 34 ")
        print("Numero de Oxidacion: +2,+4.+6 ")
        print("Masa Atomica: 78.96 umas")
        print("Configuracion Electronica:[[Ar] 3d104s24p4]") 
            
    if __name__ == '__main__':
        menu_secundario4()
    
#Halogenos   
def accion5():
    def mostrar_menu(opciones):
        print('Seleccione el tipo de elemento que desea buscar:')
        for clave in sorted(opciones):
            print(f' {clave}) {opciones[clave][0]}')

    def leer_opcion(opciones):
        while (a := input('Opción: ')) not in opciones:
            print('Opción incorrecta, selecione una de las opcionnes senaladas.')
        return a

    def ejecutar_opcion(opcion, opciones):
        opciones[opcion][1]()

    def generar_menu(opciones, opcion_menu_principal):
        opcion = None
        while opcion != opcion_menu_principal:
              mostrar_menu(opciones)
              opcion = leer_opcion(opciones)
              ejecutar_opcion(opcion, opciones)
              print()

    def menu_secundario5():
        opciones = {
        "1": ("Fluor [F]", accion1),
        "2": ("Cloro [Cl]", accion2),
        "3": ("Bromo [Br]", accion3),
        "4": ("Yodo [I]",accion4),
        "5": ("Retorno Menu Principal", menu_principal)
        }
        generar_menu(opciones,"8")
    def accion1():
        print("Fluor [F]")
        print("Numero de Electrones: 9 ")
        print("Numero de Oxidacion: +1,+3,+5,+7 ")
        print("Masa Atomica: 18 umas")
        print("Configuracion Electronica:[[He] 2s22p5]")
        
    def accion2():
        print("Cloro [Cl]")
        print("Numero de Electrones: 17 ")
        print("Numero de Oxidacion: +1,+3,+5,+7")
        print("Masa Atomica: 35,45 umas")
        print("Configuracion Electronica:[[He] 3s2 3p5]")
        
    def accion3():
        print("Bromo [Br]")
        print("Numero de Electrones: 35 ")
        print("Numero de Oxidacion: +1,+3,+5,+7")
        print("Masa Atomica:  79.90 umas")
        print("Configuracion Electronica:[[Ar] 4s²3d¹⁰4p⁵]")
        
    def accion4():
        print("Yodo [I]")
        print("Numero de Electrones: 53 ")
        print("Numero de Oxidacion: -1,+1,+3,+5") 
        print("Masa Atomica:126.90447  umas")
        print("Configuracion Electronica:[[Kr] 4d10 5s2 5p5]")
            
    if __name__ == '__main__':
        menu_secundario5()
    
#Gases Nobles    
def accion6():
    def mostrar_menu(opciones):
        print('Seleccione el tipo de elemento que desea buscar:')
        for clave in sorted(opciones):
            print(f' {clave}) {opciones[clave][0]}')

    def leer_opcion(opciones):
        while (a := input('Opción: ')) not in opciones:
            print('Opción incorrecta, selecione una de las opciones senaladas.')
        return a

    def ejecutar_opcion(opcion, opciones):
        opciones[opcion][1]()

    def generar_menu(opciones, opcion_menu_principal):
        opcion = None
        while opcion != opcion_menu_principal:
              mostrar_menu(opciones)
              opcion = leer_opcion(opciones)
              ejecutar_opcion(opcion, opciones)
              print()

    def menu_secundario6():
        opciones = {
        "1": ("Helio [He]", accion1),
        "2": ("Neon [Ne]", accion2),
        "3": ("Argon [Ar]", accion3),
        "4": ("Kripton [Kr]",accion4),
        "5": ("Xeon [Xe]",accion5),
        "6": ("Radon [Rn]",accion6),
        "7": ("Retorno Menu Principal", menu_principal)
        }
        generar_menu(opciones,"8")
    def accion1():
        print("Helio [He]")
        print("Numero de Electrones: 2 ")
        print("Masa Atomica: 4 umas")
    
        
    def accion2():
        print("Neon [Ne]")
        print("Numero de Electrones: 10 ")
        print("Masa Atomica: 20.17 umas")
        
    def accion3():
        print("Argon [Ar]")
        print("Numero de Electrones: 18 ")
        print("Masa Atomica:  38.94 umas")
       
    def accion4():
        print("Kripton [Kr]")
        print("Numero de Electrones: 36 ")
        print("Masa Atomica:83.79  umas")
    
    def accion5():
        print("Xeon [Xe]")
        print("Numero de Electrones: 54 ")
        print("Masa Atomica:131.293  umas")
    
    def accion6():
        print("Radon [Rr]")
        print("Numero de Electrones: 86 ")
        print("Masa Atomica:222 umas")
        
    if __name__ == '__main__':
        menu_secundario6()
        
def salir():
    print("Fin del Programa")

if __name__ == '__main__':
    menu_principal()
   