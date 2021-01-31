'''Crie um programa que leia a idade e o sexo de várias pessoas. a cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. no final, mostre:
Quantas pessoas tem mais de 18 anos.
Quantas homens foram cadastrados.
Quantas mulheres tem menos de 20 anos.'''
print('-' * 20)
print('CADASTRE PESSOAS')
print('-' * 20)
pa = mn = th =0
while True:
    i = int(input('Idade: '))
    if i > 18:
        pa += 1
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo: M/F ')).strip().upper()
        if s == 'M':
            th += 1
        elif s == 'F':
            if i < 20:
                mn += 1
    c = ' '
    while c not in 'SN':
        c = str(input('Quer continuar? S/N ')).strip().upper()
    if c == 'N':
        break
print(f'Foram cadastradas {pa} pessoas com mais de 18 anos')
print(f'{th} homens')
print(f'{mn} mulheres com menos de 20 anos')
