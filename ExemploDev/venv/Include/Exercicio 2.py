# 1) Utilize a linguagem Python com o comando “if, elif e else” para criar um algoritmo que receba uma idade como valor de entrada e informe se a pessoa é menor (idade < 18), adulta (idade > 18 e Idade < 60) ou idosa (Idade > 60).

idade = int(input(" Informe a idade : "))
if (idade <= 18 ) :
	print(" Você é de menor ! ")
elif(idade >= 18) and (idade <= 60) :
	print(" Você é adulto ! ",end=" ")
else :
	print(" Você é velho ! ",end=" ")
