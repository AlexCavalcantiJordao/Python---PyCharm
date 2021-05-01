n1 = int(input(" Primeiro número : "))
n2 = int(input(" Segundo número : "))
if (n1 > n2):
    print(" O primeiro é maior {} do que {} segundo.".format(n1,n2))

elif(n2 > n1):
    print(" O segundo é maior {} do que {} primeiro.".format(n1,n2))

else:
    print("{} e {} são iguais.".format(n1,n2))