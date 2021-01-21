'''Escreva um programa que faça o computador pensar em um número inteiro entre 0 a 5 e peça ao usuário
tentar descobrir qual foi o número escolhido pelo computador.'''
from random import randint 
from time import sleep
v = 'S'
while v.upper() == 'S':
    c = randint(0, 5)
    print('-=-' * 20)
    print('Pensando em um número de 0 a 5...')
    print('-=-' * 20)
    j = int(input('Em qual número eu pensei? '))
    print('PROCESSANDO...\n')
    sleep(3)
    if c == j:
        print('VOCÊ ACERTOU! ')
    else:
        print('BOCÊ ERROU! ')
    v = str(input('Quer continuar? S/N '))
print('\n\n\n\n -------FIM---------')









