'''Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo
de triângulo será formado:
Equilátero: todos os lados iguais.
Isósceles: dois lados iguais.
Escaleno: todos os lados diferentes.'''
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if a == b == c:
        print('EQUILÁTERO') 
    elif a != b != c != a:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')



