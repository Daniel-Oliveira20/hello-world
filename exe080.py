'''Crie um programa onde o usuário possa digitar cinco valores neméricos e 
cadastre-os em uma lista. Já na posição correta de inserção (sem usar o sort()). No 
final mostre a lista em ordem.'''
l = []
for i in range(0, 5):
    n = int(input('Digite um valor: '))
    if i == 0 or i == l[len(l)-1]:
        l.append(n)
    else:
        p = 0
        while p < len(l):
            if n <= l[p]:
                l.insert(p, n)
                break
            p += 1
print(f'Os valores digitados em ordem foram {l}')
