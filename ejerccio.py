# Comentario 1
import random
palabras = []
for i in range(20):
 palabra = input(f"Ingrese la palabra" {i + 1:} )
 palabras.append(palabra)
# Comentario 2
def ordenar_por_tamaño(palabras):
 return sorted(palabras, key=len, reverse=True)
# Comentario 3
while True:
 print("\nSeleccione una opción:")
 print("1. Orden alfabético")
 print("2. Orden de tamaño, de la más larga a la más corta")
 print("3. Orden aleatorio")
 print("4. Orden inverso al ingresado")
 print("5. Orden igual al ingresado")
 print("6. Salir")

 seleccion = input("Elija una opción:" )
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
 for palabra in palabras_ordenadas
 print(palabra)