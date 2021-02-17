'''Faça um programa que leia 5 valores numéricos e guarde-os em uma
lista. No final, mostre qual foi o maior e o menor valor digitadoe as suas
respectivas posições na lista.'''
n = []
mai = men = pm = pn = 0
for i in range(0, 5):
    n.append(int(input('Digite um valor:')))
    if i == 0:
        mai = n[i]
        men = n[i]
    elif n[i] > mai:
        mai = n[i]
        pm = i
    elif n[i] < men:
        men = n[i]
        pn = i
print(f'Você digitou os valores {n}')
print(f'O maior valor digitado foi {mai} na posição {pm}')
print(f'O menor valor digitado foi {men} na posição {pn}')
