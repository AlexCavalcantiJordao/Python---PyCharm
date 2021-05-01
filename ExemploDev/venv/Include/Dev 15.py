# Faça um mini-sistema que utilize o interactive help do python. O usuario vai digitar o comando e o manual vai aparecer. Quando o ususario digitar a palavra " FIM ", o programa se encerrará.
# OBS : use core
from time import sleep

c = ("\033[n",				# 0 - SEM COR
	 "\033[n0;30;41m",		# 1 - VERMELHO
	 "\033[n0;30;42m",		# 2 - VERDE
	 "\033[n0;30;43m",		# 3 - AMARELO
	 "\033[n0;30;44m",		# 4 - AZUL
	 "\033[n0;30;45m",		# 5 - ROXO
	 "\033[n0;30",	 		# 6 - BRANCO
	 "");

def ajuda(com) :
	titulo(f" Acessando o manual do comando \'{com}\'",4)
	print(c[6],end='')
	help(com)
	print(c[0],end='')
	sleep(2)

def titulo(msg,cor=0) :
 	tam = len(msg) + 4
 	print("=-="*tam)
	print(c[cor], end='')
	print("=-="*tam)
	print(f" {msg}")
	print("~"*tam)
	print(c[0],end='')
	sleep(1)


# Programa Principal
comando = ''
while True :
	titulo(" SISTEMA DE AJUDA pyHELP",2)
	comando = str(input(" Função ou Biblioteca > "))
	if comando.upper() == " FIM " :
		break
	else:
		ajuda(comando)
titulo(" ATÉ LOGO ",1)