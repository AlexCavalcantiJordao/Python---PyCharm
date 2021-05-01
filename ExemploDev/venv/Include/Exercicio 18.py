# 6) Uma empresa com 100 funcionários deseja fazer um balanço de seus gastos mensais. Para tanto, faça um programa que realize a seguinte operação.
# Calcule a média de salários recebidos
# Informe o maior salário recebido
# Informe a quantidade de pessoas que recebem mais de 2000
# Informe a quantidade de pessoas que recebem menos de 2000
# Informe o total gasto com pagamentos
# Informe o total gasto com o fundo de garantia, considere 11% sobre o salário.

quantpessoa = int(input(" Informe quantidade de pessoas : "))
salario = float(input(" Informe quanto receber R$ : "))
gasto = float(input(" Informe total de gasto R$ : "))
gastofundo = float(input(" Quanto é a porcentagem do Fundo de Garantia ? R$ : "))

if (salario <= 2000) :
	reaj = (11/100)*salario
	gasto = salario + reaj
	print(f" {salario} O gasto de reajuste de 11% passará {gasto}")
	print(f" {quantpessoa} Foi gasto por pessoa {salario} ")

else :
	reaj = (11/100)*salario
	gastofundo = salario + reaj
	print(f" {salario} um reajuste será de 11% {gastofundo}.")
	print(f" {quantpessoa} Gasto mensalmente {gastofundo}")