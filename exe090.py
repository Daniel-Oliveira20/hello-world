'''Faça um programa que leia nome e média de um aluno, guarde também
a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.'''

aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situaçao'] = 'Aprovado'
elif aluno['media'] >= 5 and aluno['media'] < 7:
    aluno['situaçao'] = 'Em recuperação'
else:
    aluno['situaçao'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k} é {v}')
