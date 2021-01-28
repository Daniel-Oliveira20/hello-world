'''Faça um programa que leia o sexo de uma pessoa, mas só aceite
os valores M ou F.
Caso esteja errado, peça a digitação novamenteaté ter um valor correto.'''
n = 's'
while n != 'M' and n != 'F':
    n = str(input('Digite o sexo M/F ')).upper()

