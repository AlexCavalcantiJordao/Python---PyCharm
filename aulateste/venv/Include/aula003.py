numero1 = int(input(" Digite o primeiro número : "))
numero2 = int(input(" Digite o segunto número : "))
numero3 = int(input(" Digite o terceiro número : "))

if (numero1 > numero2):
    print("{} escreva na {} ordem {} crescente.".format(numero1,numero2,numero3))

elif(numero2 > numero3):
    print("{} escreva na {} ordem {} crescente.".format(numero1,numero2,numero3))

elif(numero3 > numero1):
    print(" {} escreva na {} ordem {} crescente.".format(numero1,numero2,numero3))
else:
    print("  colocar na ordem.".format(numero1,numero2,numero3))