'''Faça um programa que leia o nome completro de uma pessoa 
emostre em seguida o primeiro e o último nome separadamente.'''
nome = str(input('Digite seu nome completo: ')).strip()
rnome = nome.split()
print(f'Seu primeiro nome é: {rnome[0]}')
print(f'Seu último nome é {rnome[len(rnome)-1]}')


