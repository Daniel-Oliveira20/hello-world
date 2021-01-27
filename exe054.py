'''Crie um programa que leia o ano de nascimento de sete pessoas. No final,
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
ano = date.today().year
maior = 0 
menor = 0
for i in range(1, 8):
    an = int(input(f'Ano de nascimento da {i}º pessoa:'))
    if ano - an >= 21:
        maior += 1
    else:
        menor += 1
print(f'Ao total são {maior} maior de idade e {menor} menor de idade!')

