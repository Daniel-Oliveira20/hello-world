'''Crie um programa que tenha uma tupla única nomes de produtos e seus respectivos preços,
No final mostre uma listagem de preços organizando os dados de forma tabular.'''
tp = ('lapis', 1.75,
    'Borracha', 2,
    'Caderno', 15.90,
    'Estojo', 25,
    'Tranferidor', 4.20,
    'Compasso', 9.99,
    'Mochila', 120.32,
    'Canetas', 22.30,
    'Livro', 34.90)
print('-' * 40)
print(f'{"PREÇOS":^40}')
print('-' * 40)
for i in range(0, len(tp)):
    if i % 2 == 0:
        print(f'{tp[i]:.<30}', end=' ')
    else:
        print(f'R${tp[i]:>.2f}')
print('-' * 40)
