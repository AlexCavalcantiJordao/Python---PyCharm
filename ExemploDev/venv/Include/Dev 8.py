# Faça um programa que tenha uma funçao chamada maior (), que receba vários parâmetro com valores inteiro. Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep
def maior(* núm) :
	cont = maior = 0
	print("=-="*30)
	print("\n Analisando os valores passando... ")
	for valor in núm :
		print(f" {valor} ",end=" ",flush=True)
		sleep (0.3)
		if cont == 0 :
			maior = valor
		else :
			if valor > maior :
				maior = valor
		cont += 1
	print(f" Foram informado {cont} valores ao todo. ")
	print(f" O maior valor informado foi {maior}. ")

# Programa Principal
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()