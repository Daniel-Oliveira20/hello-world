'''Faça um programa que leia nome e peso de várias pessoas, guardando
tudo em uma lista. No final, mostre:
Quantas pessoas foram cadastradas.
Uma listagem com as pessoas mais pesadas.
Uma listagem com as pessoas mais leves.'''
temp = []
p = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso Kg: ')))
    if len(p) == 0:
        mai = temp[1]
        men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        elif temp [1] < men:
            men = temp[1]
    p.append(temp[:])
    temp.clear()
    r = str(input('Quer continuar? S/N ')).upper()
    while r not in 'SN':
        r = str(input('Quer continuar? S/N ')).upper()
    if r == 'N':
        break
print(f'Foram cadastradas: {len(p)} pessoas.')
print(f'O maior peso cadastrado foi {mai} peso de ', end='')
for i in p:
    if i[1] == mai:
        print(f'{i[0]} ', end='')
print(f'\nO menor peso cadastrado foi {men} peso de ', end='')
for i in p:
    if i[1] == men:
        print(f'{i[0]} ', end='')
print()
