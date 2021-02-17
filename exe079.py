'''Crie um programa onde o usuário possa digitar vários valores númericos
e cadastre-os em uma lista. Caso o número já exista dentro da lista, não será adicionado. No
final, serão exibidos todos os números em ordem crescente.'''
n = list()
while True:
    l = int(input('Digite um valor: '))
    if l not in n:
        n.append(l)
        print('Númeoro adicionado com sucesso! ')
    else:
        print('Número já existente na lista! ')
    r = str(input('Quer continuar? S/N')).upper()
    if r == 'N':
        break
n.sort()
print(f'Em ordem, você digitou os valores: {n}')
