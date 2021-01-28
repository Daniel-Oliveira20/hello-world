'''Escreva um programa que leia um número n inteiro qualquer e mostre todos
os n primeiros elementos de uma sequência de Fibonacci.'''
n = int(input('Quantos termos quer mostrar? '))
t3 = 0
t1 = 0
t2 = 1
c = 1
while c <= n:
    print(t3, end=' ')
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    c += 1 
