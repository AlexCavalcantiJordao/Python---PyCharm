# Escreva um programa que mostre todos os números pares de 1 até 100.
par = 0
cont = 0
for par in range(0,100):
    if (par % 2 == 0):
        cont += 1
        par += cont
print(f" Número {cont} valores {par}")