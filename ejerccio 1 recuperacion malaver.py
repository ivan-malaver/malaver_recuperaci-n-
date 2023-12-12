import random
import math
N = 1000
A= [ ]
for i in range(N):
 val = random.randint(0,511)
 A.append(val)


Max_cod=255
Min_cod=0
Max_vol=12
min_vol=0


N=10
A=[]
for i in range(N):
    val=random.randint(0,255)
    A.append(val)
print(i," ", val)
print(A)

max_medicion=max(A)
min_medicion=min(A)

A.sort(reverse=False)
max_medicion=A[-1]
min_medicion=A[0]

#print("Max=", max_medicion)
#print("Min=", min_medicion)

b=min_vol
m=Max_vol/Max_cod

voltaje_max=m*max_medicion+b
voltaje_min=m*min_medicion+b
print("V_Max=", voltaje_max)
print("V_Min=", voltaje_min)

suma=0
for i in range(len(A)):
    suma=suma+A[i]
promedio=suma/len(A)
print("Promedio=", promedio*m+b)

#RMS
cuadrados=[]
for i in range(len(A)):
    cuadrados.append(A[i]**2)

suma_cuadrados=0
for i in range(len(A)):
    suma_cuadrados=suma_cuadrados+cuadrados[i]

Vrms=math.sqrt(suma_cuadrados/len(A))
print("Vrms= ", Vrms*m+b)
print(A)
 #print(A)
 