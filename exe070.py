'''Crie um programa que leia o nome e o preço de vários
produtos. O programa deverá perguntar se o usuário vai ou não 
continuar. No final, mostre:
Qual é o total gasto na compra.
Quantos produtos custam mais de R$1000.
Qual é o nome do produto mais barato.'''
t = mil = mp = 0
pb = ' '
cont = 0
print('=' * 20)
print('LOJA DE ELETRONICOS')
print('=' * 20)
while True:
    print('-' * 30)
    n = str(input('Nome do produto: ')).strip().lower()
    p = float(input('Preço: R$'))
    print('-' * 30)
    cont += 1
    if cont == 1:
        mp = p
        pb = n
    t += p
    if p > 1000:
        mil += 1
    elif p < mp:
        pb = n
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? S/N')).strip().upper()
    if c == 'N':
        break
print(f'O valor toral das compras: {t}')
print(f'{mil} produtos acima dos R$1000')
print(f'O produto mais barato: {pb}')
