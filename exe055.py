'''Faça um programa que leia o peso de cinco pessoas. No fianl,
mostre qual foi o maior e o menor peso lidos.'''
for i in range(1, 6):
    p = float(input(f'Digite o peso da {i}º pessoa: Kg: '))
    if i == 1:
        maior = p
        menor = p 
    else:
        if p > maior:
            maior = p
        elif p < menor:
            menor = p
print(f'O maior peso foi: {maior}Kg\nO menor peso foi: {menor}Kg')


