import random
from unittest import case
N=1000
A=[]
for i in range(N):
    val=random.randint(0,255)
    A.append(val)
    print(A)
   
suma_A=0
for A1 in A:
    suma_A +=A
print(A1)
Res=int(input("escriba la opcion para desarrollar: 1 para Tension Maxima 2 .para tension minima,  3Para tension promedio en voltios "))
match = Res
case = 1
Vave= A[2]*(0.707)
print(Vave)
#case = "2"
#VM= A*(0.606)
#print(VM)
#case = "3"
#VM= A/(0.707)
#print(VM)