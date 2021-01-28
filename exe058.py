from random import randint 
'''Melhore o jogo do DESAFIO 28 onde o computador vai pensar em um número
entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantas tentarivas foram necessárias para vencer.'''
from time import sleep
v = 'S'
i = 0
while v.upper() == 'S':
    c = randint(0, 10)
    print('-=-' * 20)
    print('Pensando em um número de 0 a 10...')
    print('-=-' * 20)
    j = int(input('Em qual número eu pensei? '))
    print('PROCESSANDO...\n')
    sleep(2)
    if c == j:
        v = 'N'
        print('VOCÊ ACERTOU! ')
        print(f'Foram necessarias {i + 1} tentativas')
    else:
        print('VOCÊ ERROU! ')
        v = str(input('Quer continuar? S/N '))
        i += 1
