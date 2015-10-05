#Tarea3
#License by : Karl A. Hines
#Numeros triangulares

numero = int(input("Introduzca el numero: "))
respuesta={}
for i in range(1,numero+1):
	respuesta[i]=(i*(i+1)/2)
 
for i in respuesta:
	print (i,respuesta[i])