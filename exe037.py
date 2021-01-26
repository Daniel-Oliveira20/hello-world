'''Escreva um programa que leia um número inteiro qualquer e peça
para o usuário escolher qual será a base de conversão: binário, octal ou hexadecimal.'''
n = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para convesão: ')
print('''[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opc = int(input('Sua opção: '))
if opc == 1:
    print(f'{n} convertido para binário é: {bin(n)[2:]}')
elif opc == 2: 
     print(f'{n} convertido para octal é: {oct(n)[2:]}')
elif opc == 3:
     print(f'{n} convertido para hexadecimal é: {hex(n)[2:]}')
else:
    print('OPÇÃO INVALIDA!')


