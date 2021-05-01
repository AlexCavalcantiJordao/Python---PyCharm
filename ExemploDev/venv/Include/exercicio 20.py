#  8) O IBGE está fazendo uma pesquisa sobre as características da população do Rio de Janeiro. Para tanto, eles fizeram uma pesquisa com 2000 pessoas e desejam saber as seguintes informações:
# a) Quantidade de pessoas do sexo masculino
# b) Quantidade de pessoas do sexo feminino
# c) Maior idade entre o sexo masculino
# d) Maior idade entre o sexo feminino
# e) Maior idade entre os habitantes
# f) Porcentagem de pessoas do sexo masculino
# g) Porcentagem de pessoas do sexo feminino
# h) Qual dos dois sexos é aparece em maior número na pesquisa

quanti_pessoa = masc = fem = quantmasc = quantfemi = idademasc = idadefem = maiorhabit = maiormasc = maiorfem = sexomasc = sexofem =  porcemasc = porcfem = 0
while True :
	idade = int(input(" Entre com a idade : "))
	if idade == 0 :
		break

	elif idade < 1 :
		print(" Idade inválida, tente novamente. ")
		continue

	while True :

	# Quantidade de masculino
		quanti_pessoa = str(input(" Entre com quantidade de sexo : ".format(quantmasc,quantfemi,idademasc,idadefem,maiorhabit,maiormasc,maiorfem,sexomasc,sexofem)).upper())
		if (quanti_pessoa == " quantmasc ") :
			idademasc += 1
		if (idade <= 30) :
			idademasc
			masc += 1
		elif (idade >= 40):
			idademasc
		elif (quanti_pessoa == " S ") :
			quantmasc += 1

	# Porcentagem Masculino
		elif (porcemasc/quantmasc)*quanti_pessoa :
			print(" Qual á porcentagem do sexo masculino ? : ")


	# Quantidade de feminino
		if (quanti_pessoa == " quantfem ")	:
			idadefem += 1
			quantfemi
			fem += 1
		elif (idade <= 20) :
			idadefem
		elif (idade >= 50) :
			idadefem += 1
		elif (quanti_pessoa == " S ") :
			quantfemi

	# Porcentagem Feminino
		elif (porcfem/quantfemi)*quanti_pessoa :
			print(" Qual á porcentagem do sexo feminino ? : ")

else :

	# Quantos Habitantes
	if (quanti_pessoa + quantmasc + quantmasc + maiorhabit) :
		print(" Quantos habitantes tem no Rio de janeiro ao todos ? : ")