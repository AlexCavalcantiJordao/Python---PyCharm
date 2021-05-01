# 3) Utilize a linguagem Python para escrever um programa que leia 2 valores e verifique qual deles é o maior.
primeiro = int(input('Primeiro numero: '))
segundo  = int(input('Segundo numero : '))
# Achando o maior número
maior = primeiro

if (segundo > maior):
	maior = segundo
print('Maior: ',maior)

# Achando o menor número
menor = primeiro

if (segundo < menor):
    menor = segundo

print('Menor: ',menor)