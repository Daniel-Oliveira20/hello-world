'''Faça um programa que leia um ângulo qualquer e mostre na tela 
o valor do seno, cosseno e tangente desse angulo'''
from math import cos, sin, tan, radians
an = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(an))
cosseno = cos(radians(an))
tangente = tan(radians(an))
print('Seno: {:.2f}\nCosseno: {:.2f}\nTangente: {:.2f} '.format(seno, cosseno, tangente))



