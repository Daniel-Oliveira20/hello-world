'''Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras em maiúsculo e minúsculos.
Quantas letras ao todo (sem considerara espaços).
Quantas letras tem o primeiro nome.'''
n = str(input('digite seu nome completo: ')).strip()
print('analisando seu nome...')
print('seu nome em maiuscolos é: {} '.format(n.upper()))
print('seu nome em minusculos é: {} '.format(n.lower()))
print('seu nome tem {} letras '.format(len(n)-n.count(' ')))
print('seu primeiro nome tem {} letras '.format(n.find(' ')))

