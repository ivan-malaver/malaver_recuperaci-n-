

from unittest import case

palabras_ordenadas=str


palabras=[]
palabra=input("ingrese la palabra ")

for i in range(0,5):
    
    palabra=input("ingrese la palabra ")
    palabras.append(palabra)
    i+1
print(f"palabras de la lista", palabras)

def ordenar_por_tamaño(palabras):
 return sorted(palabras, key=len, reverse=True)

while True:
 print("\nSeleccione una opción:")
 print("1. Orden alfabético de A-Z")
 print("2. Orden longitud de la palabra")
 print("3. Orden aleatorio noespecifico ")
 print("4. Orden inverso al ingresado la primera palabra ingresada es la ultima en aparecer ")
 print("5. igual al ingreso de las palabras ")
 print("6. Salir del programa ")

 seleccion = input(" opción de seleccion :" )
 match seleccion:
    case 1:
        palabras_ordenadas = sorted(palabras)
    case 2:
        palabras_ordenadas = ordenar_por_tamaño(palabras)
    case 3:
        random.shuffle(palabras)
        palabras_ordenadas = palabras
    case 4:
        palabras_ordenadas = list(reversed(palabras))
    case 5:
        palabras_ordenadas = palabras
    case 6:
        break
    case _:
        print("Opción no válida. Elija una opción del 1 al 6.")
 continue

print("\nPalabras ordenadas:")
for palabra in palabras_ordenadas:
 print(palabra)
    
    
    
