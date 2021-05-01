n1 = float(input(" Entre com a 1º nota : "))
n2 = float(input(" Entre com a 2º nota : "))
n3 = float(input(" Entre com a 3º nota : "))
media = (n1 + n2 + n3 )/3
if (media > 7) :
	print(" A média do aluno é : ",media,end=" ")
elif (media < 7) and (media >= 5) :
	print(" Aluno em recuperação, média : ",media,end=" ")
else :
	print(" Aluno reprovado ! ",media,end=" ")