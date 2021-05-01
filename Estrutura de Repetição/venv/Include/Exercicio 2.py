print("------------------------")
print("[1] Somar")
print("[2] Multiplicar")
print("[3] Maior")
print("[4] Novos Números")
print("[5] Sair do programas")
print("------------------------")

n = int(print(" Entre com valor de um número : "))
s = 0
for i in range (1,n+1,1):
    s = s + 1 / i
    print(f" O Resultado foi de {s}")