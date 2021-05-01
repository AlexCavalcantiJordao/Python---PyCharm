numero = list()
while True :
    n = int(input(" Digite um valor : "))
    if n not in numero :
        numero.append(n)
        print(" Valor adicionado com sucesso ! ")
    else :
        print(" Valor duplicado ! Não adicionar ")
    r = str(input(" Quer continuar ? [ S / N ] "))
    if r in "Nn" :
        break
print("_"*30)
numero.sort()
print(f" Você digitou os valores {numero}.")