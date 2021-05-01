n1 = float(input(" Digite 1º nota : "))
n2 = float(input(" Digite 2º nota :  "))
numero = int(input(" Me diga um número qualquer : "))
resultado = numero % 2
if resultado == 0 :
	print(f" O número {numero} é par.")
	m = (n1 + n2 + numero + resultado)
	print(" A sua média foi {:.1f}".format(m,))
	print(f" O número {numero} é impar.")
else :
	print(f" O número {numero} é impar.")