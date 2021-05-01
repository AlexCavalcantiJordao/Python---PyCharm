# Faça um programa que tenha uma função chamada escreva (), que receba um texto qualquer como parâmetro e mostre uma mensgem com tamanho adaptável

def escreva(msg) :
	tam = len(msg) + 4
	print("~"*tam)
	print(f"  {msg}")
	print("~"*tam)


escreva(" Alex Ramos ")
escreva(" Faeterj ")
escreva(" Faetec ")