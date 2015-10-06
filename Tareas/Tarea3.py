#Tarea3
#License by : Karl A. Hines
#Numeros triangulares

numero = int(input("Introduzca el numero: "))
numeros={}
for i in range(1,numero+1):
	numeros[i]=(i*(i+1)/2)
 
for i in numeros:
	print (i,numeros[i])