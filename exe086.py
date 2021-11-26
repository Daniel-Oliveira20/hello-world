'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores
lidos pelo teclado. No final, mostre a matriz na tela com a formatação adequada.'''
n = [[], [], []]
for i in range (1, 10):
    while len(n[0]) != 3:
        n[0].append(int(input('Digite um valor: ')))
    while len(n[1]) != 3:
        n[1].append(int(input('Digite um valor: ')))
    while len(n[2]) != 3:
        n[2].append(int(input('Digite um valor: ')))
#print(n[0])
#print(n[1])
#print(n[2])
print(n)
