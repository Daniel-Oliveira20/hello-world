'''Refaça o desafio 009, mostrando a tabuada de um número que o usuário
escolher, só que agora utilizando laço for.'''
from time import sleep
def vezes(n):
    c = 1
    for c in range (1, 10+1):
        print(f"{n} x {c} = {n*c}")
        sleep(0.5)


def escreve():
    print("-" * 13)


n = int(input("Digite um numero: "))
escreve()
vezes(n)
escreve()
