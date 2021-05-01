def voto(ano) :
	from datetime import date
	idade = 2020 - ano
	if (idade >= 16) and (idade < 18) or (idade > 65):
		return print(f'Com {idade} anos, o voto é opcional.')
	elif (idade < 16) :
		return print(f'Com {idade} anos, o voto é negado.')
	elif (idade > 18) :
		return print(f'Com {idade} anos, o voto é obrigatório.')

# Programa Principal
ano = int(input('Digite o seu ano de nascimento: '))
voto(ano)