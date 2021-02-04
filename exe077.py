'''Crie um programa que tenha uma tupla com várias palavras
(não usar acentuação). Depois disso, deverá mostrar a listagem das palavras 
e suas vogais.'''
palavras = ('aprender', 'programar', 'programador', 'engenheiro', 'linguagem', 
            'programacao', 'sistema', 'computador', 'trabalho', 'futuro', 'mercado')
for i in palavras:
    print(f'\nNa palavra {i} temos', end=' ')
    for l in i:
        if l.lower() in 'aeiou':
            print(l, end=' ')
