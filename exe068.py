'''Faça um programa que jogue par ou impar com o computador. O jogo só
será interrompido quando o jogador perder.
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''
from random import randint
print('=-' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 15)
v = 0
while True:
    c = randint(0, 10)
    j = int(input('Digite um valor: '))
    pi = str(input('Par ou Impar? P/I ')).upper()
    if pi == 'P':
        if (c + j) % 2 == 0:
            v += 1
            print('-' * 45)
            print(f'Você jogou {j} e o computador {c}. Total {j+c} deu PAR') 
            print('Você VENCEU! ')
            print('-' * 45)
        else:
            print('-' * 50)
            print(f'Você jogou {j} e o computador {c}. Total {j+c} deu IMPAR') 
            print('Você PERDEU! ')
            print('-' * 50)
            break
    elif pi == 'I':
        if (c + j) % 2 == 0:
            print('-' * 50)
            print(f'Você jogou {j} e o computador {c}. Total {j+c} deu PAR') 
            print('Você PERDEU! ')
            print('-' * 50)
            break
        else:
            v += 1
            print('-' * 50)
            print(f'Você jogou {j} e o computador {c}. Total {j+c} deu IMPAR') 
            print('Você VENCEU! ')
            print('-' * 50)
    else:
        print('OPÇÃO INVALIDA')
print(f'GAME OUVER! Você vonceu {v} vezes')
