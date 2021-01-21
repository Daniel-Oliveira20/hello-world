'''Dsesenvolva um programa que pergunte a distância de uma viagem em KM. Calcule
o preço da passagem cobrando R$0.50 por km para viagens de até 200KM e R$0.45 para viagens mais longas.'''
dv = float(input('Qual é a distância da sua viagem? '))
if dv <= 200:
    p = dv * 0.50
    print(f'Você vai percorrer {dv}KM e o preço da passagem é: R${p:.2f}')
else:
    p = dv * 0.45
    print(f'Você vai percorrer {dv}KM e o preço da passagem é: R${p:.2f}')










