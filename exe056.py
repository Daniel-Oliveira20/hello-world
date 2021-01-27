'''Desenvolva um programa que leia nome idade e sexo de 4 pessoas. No final do programa,
mostre:
A média de idade do gropo.
O nome do homem mais velho.
Quantas mulheres têm menos de 20 anos.'''
media = 0
hv = 0
mn = 0
for i in range(1, 5):
    pn = str(input(f'Digite o nome da {i}º pessoa: '))
    pi = int(input(f'Digite a idade da {i}º pessoa: '))
    ps = str(input(f'Digite o sexo da {i}º pessoa: M/F'))
    media += pi 
    if ps.upper() == 'M' and pi > hv:
        hv = pi
        hvn = pn 
    elif ps.upper() == 'F' and pi < 20:
        mn += 1
media = media / 4
print(f'A média de idade do grupo é: {media}\nO nome do homens mais velho é: {hvn}\nE {mn} mulheres tem menos de 20 anos!')



