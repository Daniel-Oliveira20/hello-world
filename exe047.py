'''Crie um programa que mostre todos os numeros pares entre 1 e 50'''
tp = 0
for i in range(0, 51):
    if i % 2 == 0:
        print(i, end=' ')
        tp += 1
print(f'entre 1 e 50 existem {tp} números pares!')

