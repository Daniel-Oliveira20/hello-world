'''Crie um programa que faça o computador jogar jokenpô com você.'''
from random import randint
from time import sleep


def vai():
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO')
    sleep(1)


c = randint(0, 2)
i = ('Pedra', 'Papel', 'Tesoura')
print('ESCOLHA SUA OPÇÃO OPÇÃO: ')
print('''[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
opc = int(input('Sua opção: '))
vai()
print('-=' * 15)
print(f'Computador jogou: {i[c]}')
print(f'Você jogou {i[opc]}')
print('-=' * 15)
if c == 0:
    if opc == 0:
        print('Deu EMPATE!')
    elif opc == 1:
        print('Você VENCEU!')
    elif opc == 2:
        print('Computador VENCEU')
    else:
        print('Jogada invalida!')
elif c == 1:
    if opc == 0:
        print('Computador VENCEU!')
    elif opc == 1:
        print('Deu EMPATE!')
    elif opc == 2:
        print('Você VENCEU')
    else:
        print('Jogada invalida!')
elif c == 2:
    if opc == 0:
        print('Você VENCEU!')
    elif opc == 1:
        print('Computador VENCEU!')
    elif opc == 2:
        print('Deu EMPATE!')
    else:
        print('Jogada invalida!')







