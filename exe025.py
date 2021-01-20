'''Faça um programa que verifica se existe silva em um nome digitado pelo usuário.'''
nome = str(input('Qual seu nome completo? ')).strip()
print('Sunome tem silva? {} '.format('SILVA' in nome.upper()))
