# 8) Um banco disponibiliza empréstimos as pessoas físicas seguindo o seguinte critério de juros simples:
#
# Número de parcelas menor ou igual a 12, taxa de 1.4% ao mês.
# Número de parcelas maior que 12 e menor  25, taxa de 1.8% ao mês.
# Número de parcelas maior que 24, taxa de 2.2% ao mês.
#
# Crie um algoritmo que dado o valor e o número de parcelas para pagamento, exiba o valor total e o valor pago em cada parcela.
#
# Considere a fórmula:
# Juros = ((taxa* número_parcelas) / 100) * valor_empréstimo
# Total  = valor_empréstimo + Juros
# Valor parcelas  = Total/ número_parcelas

casa = float(input(" Valor da casa R$ : "))
salario = float(input(" Salário do comprador R$ :"))
ano = int(input(" Quantos anos financiando ? : "))
prestação = casa / (ano * 12)
minimo = salario * 30 / 100
print(" Para pagar uma casa de R$ {:.2} e {} anos. ".format(casa, ano),end=" ")
print(" A prestação seráde R$ {:.2}".format(prestação))
if prestação <= minimo :
	print(" Emprestimo pode ser CONCEDIDO ! ")
else:
	print(" Empréstimo NEGADO ! ")