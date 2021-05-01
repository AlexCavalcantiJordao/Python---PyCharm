# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante á função input() do python, só que fazendo a validação para aceitar um valor numerico.
# Exemplo : n = leiaInt(" Digite um n  : ")
# Programa Principal
# n = leia(" Digite um número : ")
def leiaInt(msg) :
	ok = False
	valor = 0
	while True :
		n = str(input(msg))
		if n.isnumeric() :
			valor = int(n)
			ok = True
		else :
			print("\033]0;31mERRO ! Digite um número inteiro válido.\033[0;31m ")
			if ok :
				break
		return valor


# Programa Principal
n = leiaInt(' Digite um número : ')
print(f" Você acabou de digitar o número {n}.")