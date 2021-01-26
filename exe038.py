'''Faça um programa que leia 2 valores inteiros e compares se são maior e menor ou se são iguais.'''
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
if n1 > n2:
    print(f'O número {n1} é maior que o número {n2}!')
elif n2 > n1:
    print(f'O número {n2} é maior que o número {n1}!')
else:
    print('NUMEROS IGUAIS!')



