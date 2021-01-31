'''Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando o número
solicitado for negativo.'''
while True:
    tb = int(input('Tabuada do número: '))
    if tb < 0:
        break
    print('-' * 20)
    for i in range(1, 11):
        print(f'{tb} X {i} = {tb*i}')
    print('-' * 20)
