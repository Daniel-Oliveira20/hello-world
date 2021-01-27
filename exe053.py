'''Crie um programa que leia uma frase e diga se ela é ou não um palindromo.'''
f = str(input('Digite uma frase: ')).strip().lower()
p = f.split()
j = ''.join(p)
i = ''
for c in range (len(j) - 1, -1, -1):
    i += j[c]
print(f'A frase {f} ao contrario fica: {i}')
if i == f:
    print('È um palindromo!')
else:
    print('Não é palindromo!')
