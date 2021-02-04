'''Crie um programa que vai gerar cinco númeoros aleatórios e colocar em uma
tupla. Depois disso, mostre a listagem de númeors gerados e também indique
o maior e o menor valor que estão na tupla.'''
from random import randint
maior = menor = 0
i = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
for c in range(1, len(i)):
    if c == 1:
        maior = i[c]
        menor = i[c]
    if i[c] > maior:
        maior = i[c]
    elif i[c] < menor:
        menor = i[c]
print(i)
print(f'O maior valor {maior}')
print(f'O menor valor {menor}')
