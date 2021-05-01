num = list()
pares = list()
impares = list()
while True :
    num.append(int(input(" Digite um número : ")))
    resp = str(input(" Quer continuar ? [S/N] : "))
    if resp in "Nn" :
        break
for i, c in enumerate(num) :
    if i % 2 == 0 :
        pares.append(i)
    elif i % 2 == 1 :
        impares.append(i)
print("-="*30)
print(f" A lista completa. ")
print(f" A lista de pares é {pares}.")
print(f" A lista de impares é {impares}.")