'''Faça um programa que leia um número inteiro e diga se ele é ou não primo'''
vp = 0
n = int(input('Digite um número inteiro: '))
for i in range(1, n + 1):
    if n % i == 0:
        vp += 1
if vp <= 2:
    print(f'{n} é primo!')
else:
    print(f'{n} não é primo!')


        
    




