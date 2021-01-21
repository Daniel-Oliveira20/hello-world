'''Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu 
aumento. Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.'''


s = float(input('Qual é o salário do fincionário? R$'))
if s < 1250:
    s = s + (s * 15 / 100)
else:
    s = s + (s * 10 / 100)
print(f'O salário passa a ser de: R${s}')








