'''Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vezes aparece a letra A.
Em que posição ela aparece a primeira vez.
Em que posição ela aparece a última vez.'''
frase = str(input('Insira sua frase: ')).strip().lower()
print(f'A letra "a" aparece {frase.count("a")} vezes')
print(f'A letra "a" aparece a primeira vez na posição {frase.find("a") + 1}')
print(f'A ultima letra "a" aparece na {frase.rfind("a") + 1}')
