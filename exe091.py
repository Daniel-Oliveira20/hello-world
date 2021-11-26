'''Crie um programa onde 4 jogadores joguem um dado e tenham resultados
aleatórios. Guarde esses resultados em um dicionário. No final coloque esse
dicionário em ordem, sabendo que o vencedor tirou o maior número.'''
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
         'jogador2': randint(1,6),
         'jogador3': randint(1,6),
         'jogador4': randint(1,6)
}
ranking = []
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'O {k} tirou: {v}')
    sleep(0.5)
print('Ranking dos jogadores: ')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, j in enumerate(ranking):
    print(f'{i+1} lugar: {j[0]} com {j[1]}')
    sleep(1)
