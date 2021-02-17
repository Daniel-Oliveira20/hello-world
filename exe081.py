'''Crie um programa que vai ler vários números e colocar em uma lista. Depois
disso, mostre:
Quantos números foram digitados.
A lista em ordem decrecente.
se o valor 5 foi digitado e está ou não na lista.'''
l = list()
while True:
    v = int(input('Digite um valor: '))
    l.append(v)
    r = str(input('Quer continuar? S/N ')).upper()
    if r == 'N':
        break
print(f'Você digitou {len(l)} elementos')
l.sort(reverse=True)
print(f'Os valores em ordem decrecente: {l}')
if 5 in l:
    print('O valor 5 faz parte da lista! ')
else:
    print('O valor 5 não faz paarte da lista!')
