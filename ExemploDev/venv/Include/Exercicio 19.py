#  7) Siga as instruções para elaboração do algoritmo abaixo:
#
# a) Imprima a soma de  todos os múltiplos de 3 de 1 até 300.
# b) Imprima a soma do quadrado de todos os múltiplos de 4 de 1 até 300.
# c) Imprima a soma das divisões por 2 de todos os múltiplos de 6 de 1 até 300.
# d) Imprima a soma de todos os múltiplos de 10 de 1 até 300.
num = cont = soma = divi = 0
print("=-="*20)

num = int(input(" Digite um número : "))
for num in range (3,1,300) :
	soma += cont
	cont += 1
	num = int(input(" Digite um número : "))
print(f" Você digitou {soma} número e a soma entre eles foi {cont}")
print('=-='*20)

cont = int(input(' Digite um número :'))
for cont in range(4,1,300) :
	cont += soma
	cont += 1
	cont = int(input(" Digite um número : "))
print(f" Você digitou {soma} número e a soma entre eles foi {cont} ")

print('=-='*20)

num = int(input(" Digite um número : "))
for soma in range(10,1,300) :
	divi += soma
	cont += 1
	cont = int(input(" Digite um número : "))
	cont = (num + soma + cont + divi)
print(f" Você digitou {divi} número e a soma entre eles foi {soma}")
print(f' A soma entre eles foram {cont}, {num}')


print("=-="*20)