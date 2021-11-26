'''Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno
retangular (largura e altura) e mostre a área do terreno.'''
def area(x, y):
    return x * y


print('CNTROLE DE TERRENO')
print('--------------------')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
print(f'A área de um terreno {l}x{c} é de {area(l,c)}m2')
