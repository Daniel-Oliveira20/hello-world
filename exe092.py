'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho
e cadastre-os (com idade) em um dicionário se por acaso a CTPS for diferente de 0,
o dicionário receberá também o ano de contratação e o salário. Calcule e
acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime
dado = {}
dado['nome'] = str(input('Nome: '))
an = int(input('Ano de nascimento: '))
dado['idade'] = datetime.now().year - an
dado['carteira'] = str(input('Carteira de trabalho: [0] = não tem '))
if dado['carteira'] != '0':
    dado['anoc'] = int(input('Ano de contratação: '))
    dado['salario'] = float(input('Salário: '))
    dado['aposentadoria'] = dado['idade'] + ((dado['anoc'] + 35) -datetime.now().year)
else:
    for k, v in dado.items():
        print(f'{k} {v}')

for k, v in dado.items():
        print(f'{k} {v}')
