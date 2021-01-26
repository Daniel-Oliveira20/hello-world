'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o
preço normal e condições de pagamento.'''
pc = float(input('Qual o preço das compras? R$'))
print("""FORMA DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão 
[ 4 ] 3x ou mais no cartão""")
opc = int(input('Qual é a opção? '))
if opc == 1:
    total = pc - (pc * 10 / 100)
elif opc == 2:
    total = pc - (pc * 5 / 100)
elif opc == 3:
    total = pc
    par = total / 2
    print(f'A compra será parcelada em 2x de R${par:.2f} SEM JUROS!')
elif opc == 4:
    total = pc + (pc * 20 / 100)
    totalpar = int(input('Quantas parcelas? '))
    par = total / totalpar 
    print(f'A compra de R${pc} será parcelada em {totalpar}x de R${par:.2f} COM JUROS')
else:
    print('OPÇÃO INVALIDA, COMECE NOVAMENTE')
print(f'A compra de R${pc} vai custar R${total} reais no final ')



















