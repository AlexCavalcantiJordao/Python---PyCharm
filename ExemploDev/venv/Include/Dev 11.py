# Crie um programa que tenha uma função fatorial() que receba dois parametro : o 1º que calcular e o outro chamado show, que será um valor lógico (opcional) indicando se será mostrando ou não na tela processo de cálculo do fatorial."print(fatorial(5)) ou true"
def Fatorial(n,show=False) :
	"""
	-> Calcular o Fatorial de um número
	:param n:  O número a ser calculado
	:param show: Opcional () Mostrar ou não a conta
	:return: O valor do fatorial de um número n.

	"""
	f = 1
	for c in range(n,0, -1) :
		if show :
			if c > f :
				print(" x ",end=" ")
			else:
				print(" = ",end=" ")
		f *= c
		return f


# Programa Principal
print(Fatorial(5,show=False))
