'''Desenvolva um programa que leia quatro valores pelo teclado grarde-os em uma
tupla. No final, mostre:
Quantas vezes o número 9 aparece.
Em que posição foi digitado o valor 3.
Quais foram os números pares.'''
n = (int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: ')))
print(n)
print(f'O número 9 apareceu: {n.count(9)}')
if 3 in n:
    print(f'O número 3 apareceu na posição {n.index(3)+1} ')
else:
    print('O valor 3 não foi digitado ')
print('Os valors pares: ')
for i in range(1, len(n)):
    if n[i] % 2 == 0:
        print(n[i], end=' ')
