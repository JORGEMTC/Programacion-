def base():
    print("Base: ")
    return base
base()
b=int(input())
def exponente():
    print("Exponente: ")
    return exponente
exponente()
e=int(input())

if b<0 and e>0:
    print("Error...!")
    print("Fin del Programa")
if b>0 and e<0:
   print("Error...!")
   print("Fin Programa")   
if b<0 and e<0:
   print("Error...!")
   print("Fin Programa")
else:
    b>0 and e>0    
    potencia=b**e 
    print("\n Respuesta",potencia)
