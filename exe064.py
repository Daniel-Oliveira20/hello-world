'''Crie um programa que leia vários números inteiros pelo teclado parando apenas quando for
digitado 999. No final, mostre quantos números foram digitados e qual é a soma entre eles,
desconsiderando o 999.'''
c = 0
t = 0
n = 0
while n != 999:
    n = int(input('Digite um numero (999 para parar): '))
    if n == 999:
        break
    t += n
    c += 1
print(f'Você digitou {c} números e a soma dos números digitados é: {t}')
