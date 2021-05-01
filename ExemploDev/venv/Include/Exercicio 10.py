# 10) - Faça um programa que receba um número via teclado e verifique se este número é par ou ímpar.
print("=-="*15)
numero = int(input(" Digite um número para saber ser ele é par ou impar : "))
resto = numero % 2
if resto == 0:
	print(" Número é par ")
else :
	print(" Número é impar ")
print("=-="*15)