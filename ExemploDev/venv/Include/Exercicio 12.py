# Escreva um programa que mostre todos os números impares de 1 até 100.
impar = 0
cont = 0
for par in range(1,100):
    if (par % 2 == 1):
        cont += 1
        par += cont
print(f" Número {cont} valores {impar} impares.")