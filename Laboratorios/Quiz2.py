#Quiz2
#License by : Karl A. Hines
#Compra

cliente = 0

while cliente < 5:
	compra = float(input("Cliente: "))

	cliente += 1

	if compra >= 500:
		desc = compra * 0.30
		subt = compra - desc
		total = subt
		print("Su monto a pagar es: {0} " .format(total))

	elif compra < 500 and compra >= 200:
		desc = compra * 0.20
		subt = compra - desc
		total = subt
		print("Su monto a pagar es: {0} " .format(total))

	elif compra < 200 and compra >= 100:
		desc = compra * 0.10
		subt = compra - desc
		total = subt
		print("Su monto a pagar es: {0} " .format(total))

	else:
		print("No tiene descuento")
else:
	print("Gracias por comprar en el EMPERADOR")	