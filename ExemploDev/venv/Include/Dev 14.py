# Faça um programa que tenha uma função notas() que pode receber vários notas de alunos e vai retornar um dicionario com as seguintes informação :
# Quantidades de notas
# A maior nota
# menor nota
# A média da turma
# a situação (Opcional)
def notas(*n,sit = False) :
	"""
	-> FUNÇÃO para analisar notas e situção de vários alunos.
	:param n: uma ou mais dos alunos (aceita vários).
	:param sit: valor opcional,indicando se deve ou não adicionar a situção.
	:return: adicionar com vários informações sobre situção da turma.
	"""



	r = dict()
	r['total'] = len(n)
	r['maior'] = len(n)
	r['menor'] = len(n)
	r['média'] = sum(n)/len(n)

	if sit :
		if r['média'] >= 7 :
			  r['situação'] = 'BOA'
		elif r['média'] >= 5 :
			r['situação'] = 'RAZOAVEL'
		else:
			r['situação'] = 'RUIM'
	return r


# Programa Principal
resp = notas(5.5,9.5,10,6.5)
print(resp)