# Utilize o comando while para criar um programa que receba 4 nota de cada aluno do curso de sistema de informação e calcule a média de cada aluno.
nota1 = int(input(" Digite a 1º nota : "))
nota2 = int(input(" Digite a 2º nota : "))
nota3 = int(input(" Digite a 3º nota : "))
nota4 = int(input(" Digite a 4º nota : "))
media = (nota1 + nota2 + nota3 + nota4)/2
print(" A média entre {:.1f} e {:.1f} é igual a {:.1f}".format(nota1,nota2,nota3,nota4,media))