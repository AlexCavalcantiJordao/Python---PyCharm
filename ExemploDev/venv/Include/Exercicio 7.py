# 7) Crie um algoritmo em Python que faça a conversão de valores em reais, para dólar, euro ou libra esterlina.
# 		Considere:
# 		1 dólar  =  3,94 Reais
# 		1 euro  =  4,46 Reais
# 		1 libra  =  4,74  Reais

print("=-="*25)
real = float(input(" Quando dinheiro você tem na carteira ? : "))
dolar = real / 3.94
libra = dolar / 4.46
euro = real / 4.74
print(" Com R$ : {:.2f} você pode comprar U$$ : {:.2f} , LB$ : {:.2f} e EURO$ {:.2f}".format(real,dolar,libra,euro))
print("=-="*25)