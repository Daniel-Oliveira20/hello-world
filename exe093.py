'''Crie um programa que gerencie o aproveitamento de um jogador
de futebol. O programa vai ler o nome do jogador e quantas partidas ele
jogou. Depois vai ler a quantidade de gols feitas em cada partida. No final, tudo 
isso será guardado em dicionário, incluindo o total de gols feitos durante o campeonato.'''
n = {}
n['nome'] = str(input('Nome do jogador: '))
n['partidas'] = int(input('Partidas jogadas: '))
c = 1
tg = 0
gols = []
while c <= n['partidas']:
    g = int(input(f'Gols na partida {c}: '))
    if g > 0:
        tg += g
    gols.append(g)
    c += 1
n['gols'] = gols[:]
n['total'] = tg
print('-=' * 30)
print(n)
print('-=' * 30)
for k, v in n.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
for i, v in enumerate(gols):
    print(f'Na partida {i+1}, fez {v}')
print(f'Foi um total de {tg} gols')
