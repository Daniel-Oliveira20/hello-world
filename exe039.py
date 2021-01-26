'''Faça um programa que leia o ano de nascimento de um jovem e informe se acordo com sua idade:
Se ele precisa se alistar.
Se é a hora de se alistar.
Se já passou do tempo de se alistar.'''
from datetime import date
atual = date.today().year
sexo = str(input('Qual sexo? M/F'))
if sexo.upper() == 'M':
    n = int(input('ano de nascimento? '))
    idade = atual - n 
    print(f'Quem nasceu em {n} completará {idade} anos em {atual}')
    if idade == 18:
        print('Você tem que se alistar!')
    elif idade < 18:
        print(f'Ainda faltam {18 - idade} para o alistamento!')
    else:
        print(f'Já deveria ter se alistado há {idade - 18} anos!')
else:
    print('Não precisa se alistar!') 





