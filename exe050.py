'''Desenvolva um programa que leia seis números inteiros e mostre 
a soma apenas daqueles que forem pares.'''
tp = 0
for i in range(1, 7):
    n = int(input(f'Digite o {i}º númeoro inteiro: '))
    if n % 2 == 0:
        tp = tp + n
print(f'A soma de todos os números pares digitados é: {tp}')
