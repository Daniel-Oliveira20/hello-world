'''Crie um programa que leia vários números inteiros pelo teclado. No fianl da execução,
mostre a nédia entre todos os valores e qual foi o maior e o menor número lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar.'''
n = c = s = m = me = 0
v = 'S'
while v == 'S':
    n = int(input('Digite um número: '))
    c += 1 
    s += n
    if c == 1:
        m = me = n
    else:
        if n > m:
            m = n
        elif n < me:
            me = n
    v = str(input('Quer continuar? S/N')).upper()
media = s / c
print(f'Você digitou {c} números e a média foi {media:.2f}')
print(f'O menor valor digitado foi {me} e o maior {m}')
