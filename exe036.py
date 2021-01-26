'''Escreva um programa para aprovar o emprestimo bancário para a compra
de uma casa. O programa vai perguntar o valor da casa, o salário do comprador
e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exveder 30%
do salário ou então o emprestimo será negado.'''

vc = float(input('Valor da casa: ')) 
vs = float(input('Valor do salário: '))
a = int(input('Em quanto anos vai pagar? '))
p = (vc / a) * 12
if p * 30 / 100 > vs * 30 / 100:
    print('EMPRESTIMO NEGADO!\nValor da parcela excede 30% do salario')
else:
    print('EMPRESTIMO APROVADO: ')


