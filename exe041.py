'''A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de
um atleta e mostre sua categoria de acordo com a idade.'''
from datetime import date
atual = date.today().year
n = int(input('Ano de nascimento: '))
if atual - n <= 9:
    print(f'Categoria mirim! {atual - n} anos')
elif atual - n > 9 and atual - n <= 14:
    print(f'Categoria infantil! {atual - n} anos')
elif atual - n > 14 and atual - n <= 19:
    print(f'Categoria junior! {atual - n} anos')
elif atual - n > 19 and atual - n <= 20:
    print(f'Categoria Sênior! {atual - n} anos')
else:
    print(f'Categoria master! {atual - n} anos')


