'''Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome santo'''
t = str(input('Digite a cidade em que nascewu: ')).strip()
print(t[:5].upper() == 'SANTO' )

