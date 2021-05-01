# Faça um programa que tenha uma lista chamada sorteia () e somaPar (). A primeira função vai sortear 5 número e vai coloca-os dentro da lista e a segunda função vai mostrar a soma entre os valores pares sorteados pela função anterior.
from random import randint
from time import sleep


def sorteia(lista) :
	print(" Sorteando 5 valores da Lista : ",end=" ")
	for cont in range(0,5) :
		n = randint(1,10)
		lista.append(n)
		print(f" {n} ",end=" ",flush=True)
		sleep(0.3)
	print(" PRONTO ! ")


def somaPar(lista) :
	soma = 0
	for valor in lista :
		if valor % 2 == 0 :
			soma += valor
	print(f" Somando os valores pares de {lista}, temos {soma}.")