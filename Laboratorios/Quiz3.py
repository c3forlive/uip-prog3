#Quiz3
#License by : Karl A. Hines
#Segundos a minutos

for m in range (0,5):
	tiemposec = int(input("Introduzca los segundos "))
	minutos = tiemposec/60
	if minutos != 0:
		segundos = 60-tiemposec%60
		print("Le faltan {0}, segundos para llegar al minuto".format(segundos))