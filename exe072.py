'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclardo
(entre 0 e 20) e mostra-lo por extenso.'''
ti = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        i = int(input('Digite um número entre 0 e 20: '))
        if i > 20 or i < 0:
            print('Tente novamente.', end=' ')
        else:
            break
    print(f'Voce digitou o número: {ti[i]}')
    v = str(input('Quer continuar? S/N ')).strip().upper()
    if v == 'N':
        break
