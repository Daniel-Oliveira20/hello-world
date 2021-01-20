'''Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos
separados 
ex: 
ditado um número 1834
unidade: 4 dezena: 3 centena: 3 milhar: 1'''
n = int(input('Digite um numero inteiro: '))
while n > 9999:
    print('Digite um número que seja maior que 0 e menor que 10.000')
    n = int(input('Digite um numero inteiro: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Analisando o numero {} '.format(n))
print('Unidade:{}\nDezena:{}\nCentena:{}\nMilhar: {} '.format(u, d, c, m))


