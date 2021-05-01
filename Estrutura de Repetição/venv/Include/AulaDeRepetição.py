par = 0
cont = 0
for par in range(1,50):
    if (par % 2 == 1):
        cont += 1
        par += cont
print(f" Número {cont} valores {par}")