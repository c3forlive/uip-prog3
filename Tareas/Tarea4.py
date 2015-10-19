#Tarea 4
#License by : Karl A. Hines
#Minutos, Dias y Horas

tiempo = int (input("Introduzca la cantidad de minutos: "))

dias = int (tiempo/1440)
tiempo = tiempo - dias*1440
horas = int (tiempo/60)
tiempo = tiempo - horas*60
minutos = tiempo

print(" El tiempo calculado fue de: " +str(dias) +" dias " +str(horas) +" horas " +str(minutos) +" minutos ")
