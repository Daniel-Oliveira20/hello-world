'''Desenvolva um programa que leia o primeiro termo e a razão de uma PA
no final, mostre os 10 primeiros termos dessa progressão.'''
print('=' * 35)
print('    10 TERMOS DE UMA PROGRASSÃO    ')
print('=' * 35)
n = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = n + (10 - 1) * r
for i in range(n, decimo + r, r):
    print(i, end=' ')

