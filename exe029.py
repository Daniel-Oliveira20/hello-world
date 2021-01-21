'''Escreva um programa que leia a velocidade de um carro.
Se ela ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7.00 por cada km acima do limete.'''
v = float(input('Qual é a velocidade atual do carro? '))
if v > 80:
    m = (v - 80) * 7
    print(f'MULTADO! Você excedeu o limite permitido que é de 80KM/h\nVocê deve pagar uma multa de R${m}')
print('Tenha um bom dia! Dirija com segurança! ')

