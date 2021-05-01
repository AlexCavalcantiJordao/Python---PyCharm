preco = float( input("Valor original: R$ ") )
condicao = str(input(" Forma de pagamento :"))

valor_descontado = preco / 10
valor_cartao = preco / 5
preco_normal = preco * 2
desconto = preco / 20

# Exibindo tudo
print('Valor original:     R$', preco)
print('Desconto ganho:     R$', valor_descontado)
print('desconto no cartão : R$', valor_cartao)
print(' Preço normal : R$', preco_normal)
print(' desconto de 3x ou + R$ ', desconto)



