# Faça um programa que tenha uma função chamada contador (), que receba três parâmetro com valores inteiro .Seu programa tem que realizar três contagem através da função criado :
# a) De 1 até 10, de 1 em 1
# b) De 10 até 10, de 2 em 2
# c) Uma contagem personalizado
from time import sleep


def contador (i, f, p) :
	if p < 0 :
		p *= -1
	if p == 0 :
		p = 1
	print("=-="*20)
	print(f" Contagem de {i} até {f} de {p} em {p}. ")
	sleep(2.5)

	if i < f :
		cont = 1
		while cont < f :
			print(f" {cont} ",end=" ",flush=True)
			sleep(0.5)
			cont += p
		print("FIM")
	else :
		cont = i
		while cont >= f :
			print(f" {cont} ", end=" ",flush=True)
			sleep(0.5)
			cont -= p
		print("FIM")

# Programa Principal
contador(1, 10, 1)
contador(10, 0, 2)
print("=-="*20)
print(" Agora é sua vez de personalizar a contagem ! ")
ini = int(print(" Inicio : "))
fim = int(print(" Fim :    "))
pas = int(print(" Passo :  "))
contador(ini,fim,pas)