# Faça umn programa que tenha uma função chamada ficha(), que receba dois parametros opcinais : O nome de um jogador e quantos gols ele marcou.
# O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dados não tenha sido informado corretamente.
def Ficha(jog= "< Desconhecido >",gols = 0) :
	print(f" O jogador {jog} fez {gols} no campeonato. ")

# Programa Principal
n = str(input(" Nome do jogador : "))
g = str(input(" Número de Gols : "))
if g.isnumeric() :
	g = int(g)
else :
	g = 0
if n.strip() == '' :
	ficha(gol=g)
else :
	Ficha(n,g)