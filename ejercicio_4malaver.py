 
import random
#Ivan Malaver Fierro
#codigo para realizar una lista es cadenay gyardarla para su utlizacion 
palabras_ordenadas=str


palabras=[]
#ingresar la lista de palabras que seran orednadas segun el criterio de seleccion 
palabra=input("ingrese la palabra ")
#realiza un ciclo donde guarda un rango de palabras escritas por el operador del codigo 
#este rango se puede modificar cambiando el numero de posiciones a almacenar 
for i in range(0,4):
    
    palabra=input("ingrese la palabra ")
    palabras.append(palabra)
    i+1
print(f"palabras de la lista", palabras)
#Append es un método que tiene toda lista de Python 
# el cual permite agregar un elemento al final de la lista
#la i indica el punto de partida del cliclo y se le suma un nuevo registro ingresado por usario 



def ordenar_por_tamaño(palabras):
    return sorted(palabras,key=len,reverse=True)

#ordenar por tamaño sorted() que crea una nueva lista ordenada a partir de un iterable. 
#sort() y esta se ordenará alfabéticamente en orden ascendente (a-z)


    
print("\n selecione una opcion")
print("1.Orden alfabetico")
print("2.orden de tamaño,de la mas larga a la mas corta")
print("3.orden aleatorio")
print("4.ordenar inverso al ingresado")
print("5.orden igual al ingresado")
print("6.salir")
#se imprime un menu de seleccion para guiar al usuario en su seleccion     
seleccion=int(input(print("elija una opcion ")))
    
match seleccion:
      case 1:
        palabras_ordenadas=sorted(palabras)
      case 2:
        palabras_ordenadas=ordenar_por_tamaño(palabras)
      case 3:
        random.shuffle(palabras)
        #Retorna un elemento aleatorio de una secuencia seq no vacía.
        palabras_ordenadas=palabras
      case 4:
        palabras_ordenadas=list(reversed(palabras))
      case 5:
        palabras_ordenadas=palabras
      case 6:
        palabras
      case _:
        print("opcion no valida.Elija una opcion de 1 a 6.")
        
        
        

#el comando print muestra en pantalla la operacion seleccionada  

print(f"ordenado segun la opcion anterior", palabras_ordenadas)





print("\n selecione una opcion")
print("1.Orden alfabetico")
print("2.orden de tamaño,de la mas larga a la mas corta")
print("3.orden aleatorio")
print("4.ordenar inverso al ingresado")
print("5.orden igual al ingresado")
print("6.salir")
 
    





