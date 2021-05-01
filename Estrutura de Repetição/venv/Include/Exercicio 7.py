from time import sleep
n1 = int(input(" Primeiro valor : "))
n2 = int(input(" Segundo valor : "))
opção = 0
while opção != 5 :
    print("[1] Somar")
    print("[2] Multiplicar")
    print("[3] Maior")
    print("[4] Novo Número")
    print("[5] Sair do programa")
opção = int(input(" Qual é a opção : "))
if opção == 1 :
    soma = n1 + n2
    print(f" A soma entre {n1} + {n2} é {soma}")
elif opção == 2 :
    produto = n1 * n2
    print(f" O resultado de {n1} x {n2} é {produto}")
elif opção == 3 :
    if n1 > n2 :
        maior = n1
    else:
        maior = n2
        print(f" Entre {n1} é {n2} o maior valor é {maior}")
elif opção == 4 :
    print(" Informe os números novamente : ")
    n1 = int(input(" Primeiro valor : "))
    n2 = int(input(" Segundo valor : "))