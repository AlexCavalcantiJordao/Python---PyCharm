peso = float(input(" Qual o seu peso ? (Kg) "))
altura = float(input(" Qual é sua altura ? (m) "))
imc = peso/(altura)
print(" O imc dessa pessoa é de {:.1f}".format(imc))
if imc < 18.5 :
    print(" Você está abiaxo do peso normal")
elif 18.5 <= imc < 25 :
    print(" Parabéns você está na baixo do peso normal ")
elif 25 <= imc < 30 :
    print(" Você está em sobrepeso ")
elif 30 <= imc < 40 :
    print(" Você está em obesidade ")
elif imc >= 40 :
    print(" Você está em ovesidade mórbida, cuidado ! ")