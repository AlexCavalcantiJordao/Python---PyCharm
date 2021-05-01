# 8) - Crie um algoritmo em Python que receba como entrada o peso e a altura de uma pessoa e calcule o índice de massa corporal(IMC). Descubra se a pessoa está abaixo do peso (IMC <= 18.5), peso ideal (IMC  > 18.5 e IMC <= 25) ou  acima do peso (IMC > 25).
#         Fórmula :
#         IMC =  peso /(altura * altura)

print("=-="*30)
altura = float(input(" Qual é a sua altura ? : "))
peso= float(input(" Qual é o seu peso ? : "))
imc = peso / (altura ** 2)
print("=-="*30)

print(" O IMC da pessoa é de {:.0}.".format(imc))

if (imc < 18.5) :
	print(" Você estar abaixo do peso normal ! ")

elif (imc <= 18.5) and (imc < 25) :
	print(" Você estar na faixa no peso normal !  ")

elif (imc <= 25) and  (imc < 30) :
	print(" Você estar sobrepeso ! ")

elif (imc <= 30) and (imc < 40) :
	print(" Você estar obeso ! ")

elif(imc <= 40 ) :
	print(" Você estar acima do Obesidade mórbida, cuidado !  ")