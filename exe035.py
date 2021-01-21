'''Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas 
podem ou não formar um triângulo.'''


print('-=-' * 20)
print('Analisador de triângulos')
print('-=-' * 20)

s1 = float(input('Primeiro siguimento: '))
s2 = float(input('Primeiro siguimento: '))
s3 = float(input('Primeiro siguimento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os seguimentos PODEM FORMAR um trinângulo!')
else:
    print('Os seguimentos NÃO PODEM formar um triângulo!')
