'''Faça um programa que tenha uma lista chamada números e duas funções chamadas
sorteia() e somapar(). A primeira vai sortear 5 númeors e colocalas dentro de lista e 
a segundo vai mostrar a soma de todos os valores pares dentro da lista.'''

from time import sleep
from random import randint
lista = []
def sorteia():
        n = randint(1,10)
        return n


def spar(dados):
    s = 0
    for i in list(lista):
        if i % 2 == 0:
            s = s + i
    return s


print(f'Sorteando 5 valores: ', end=' ')
for i in range(1,6):
    print(sorteia(), end=' ', flush=True)
    lista.append(sorteia())
    sleep(0.5)
print(f'\nA soma dos valores pares: {spar(lista)}')
