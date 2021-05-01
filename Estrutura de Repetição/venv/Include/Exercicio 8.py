tabuada = int(input(" Montar a tabuada do número : "))
inicio = int(input(" Comeca em : "))
while True :
    fim = int(input(" Termina em : "))
    if fim >= inicio :
        break
print(f"\n tabuada do número {tabuada} começando em {inicio} e terminando em {fim} \n")
for n in range (inicio, fim+1):
    print(f"{n} x {tabuada} = {n*tabuada}")