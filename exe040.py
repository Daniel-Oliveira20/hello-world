'''Crie um programa que leia duas notas de um aluno e calcule sua média, mostre uma mensagem final, 
de acordo com a média atingida:
Média abaixo de 5.0 REPROVADO.
Média entre 5.0 e 6.9 RECUPERAÇÃO.
Média 7.0 ou superior APROVADO.'''
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
m = (n1 + n2) / 2
if m <= 5.0:
    print(f'REPROVADO! média: {m}')
elif m > 5.0 and m < 7:
    print(f'Em recuperação! Média: {m}')
else:
    print(f'APROVADO! Média: {m}')
