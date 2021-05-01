maior,menor = 0,0
num = int(input(" Entre com um número : "))
while True :
    op = input(" Deseja continuar ? : ")
    if (op == "n") :
        break
    if (num > maior) :
        maior = num
    if (num < menor) :
        menor = menor
    num = int(input(" entre com um número : "))