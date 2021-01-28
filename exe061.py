'''Refaça o exercicio 51, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando estrutura while.'''
p = float(input('Primeiro termo: '))
r = float(input('Razão: '))
t = p 
c = 1
while c <= 10:
    print(t)
    t += r
    c += 1
print('FIM')