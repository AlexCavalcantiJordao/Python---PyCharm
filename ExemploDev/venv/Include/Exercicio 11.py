# 11) Utilize a linguagem Python com o comando “if, elif e else” para  criar um algoritmo que escolha entre calcular as áreas do quadrado, triângulo ou retângulo.
#
#        Quadrado  = Lado x Lado
#        Triângulo =  (Base x Altura)/2
#        Retângulo  =  Base x Altura
#
#      Obs: Faça uso de um verificador para escolher entre uma das operações.


def área(larg, comp) :
	a = larg * comp
	print(f" A área de um terreno {larg} x {comp} é de {a}m². ")


print(" Controle de Terreno ")
print("-"*20)
l = float(input(" LARGURA (m) : "))
c = float(input(" COMPRIMENTO (m) : "))
área(l,c)