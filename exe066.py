'''Crie um programa que leia vários números inteiros pelo teclado. O 
programa só vai parar quando o usuário digitar 999, no final, mostre
quantos valores foram digitados e a soma entre eles mas sem incluir 999.'''
c = t = 0
while True:
    n = int(input('Digite um numero (999 para parar): '))
    if n == 999:
        break
    t += n
    c += 1
print(f'Você digitou {c} números e a soma dos números digitados é: {t}')
