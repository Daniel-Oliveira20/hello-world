'''Crie um programa onde o usuário possa digitar sete valores númericos
e cadastre-os em uma lista única que mantenha separados os valores pares
e ímpares. No final, mostre os valores pares e ímpares em orde crescente.'''
n = [[], []]
for i in range(1, 8):
    np = int(input(f'Digite o {i}º valor: '))
    if np % 2 == 0:
        n[0].append(np)
    else:
        n[1].append(np)
n[0].sort()
n[1].sort()
print(f'A lista de pares: {n[0]}')
print(f'A lista de impares: {n[1]}')
