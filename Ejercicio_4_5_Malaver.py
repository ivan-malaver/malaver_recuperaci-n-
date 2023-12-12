#comentario 
#import

from unittest import case


palabra=[]
for i in range(10):
    palabra=input(f"ingrese la palabra")
    val= (i+1)
palabra.append(val)
#print(palabra)
#comentario 
def ordenar_por_tamaño(palabra):
    return sorted(palabra,key=len,reverse=True)
#comentario
while True:
    print("\nSeleccione una opcion:")
    print("1.ordenar alfabeticamente:")
    print("2.ordenar tamaño, de la mas larga a la mas corta:")
    print("3.ordenar aleatoricamente:")
    print("4.ordenar inverso al ingresar:")
    print("5.ordenar igal al ingresar:")
    print("6.salir:")
    seleccion=input("Elija una opcion:")
    match=seleccion
    case = "1"
    palabras_rodenadas =sorted(palabra)
    case = "2"
    palabras_rodenadas =ordenar_por_tamaño(palabra)
    case = "3"
    import random
    random.shufle(palabra)
    palabras_rodenadas =palabra
    case = "4"
    palabras_rodenadas =list(reversed(palabra))
    case = "5"
    palabras_rodenadas =palabra
    ordenar_por_tamaño(palabra)
    
    
    