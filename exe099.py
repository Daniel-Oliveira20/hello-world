'''Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com 
valores inteiros. Seu program tem que analisar todos os valores e dizer qual é o maior.'''
from time import sleep

def maior(* x):
    c = m = 0

    print('\nAnalisando os valores... ')
    for i in x:
        if m < i:
            m = i
        print(f'{i}', end='', flush=True)
        sleep(0.4)
        if c == 0:
            m = i
        else:
            if i > m:
                m < i
        c += 1
    print(f'Foram informados {c} valores ao todo')
    print(f'O maior valor informado foi {m}')



maior(4, 8, 4, 2, 3, 4, 7)
maior(15, 90, 26)
maior(3, 4, 8, 7, 5)
