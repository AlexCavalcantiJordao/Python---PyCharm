maior,menor = 0,0
num = int(input(" Entre com um número : "))
while True :
    op = input(" Deseja continuar ? : ")
    if op == "n" :
        break
    elif num > maior :
        maior = num
    elif num < menor :
        menor = num

