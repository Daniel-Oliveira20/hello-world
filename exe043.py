'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
seu IMC e mostre seu status, de acordo com a tabela abaixo.'''
a = float(input('Digite sua altura: '))
p = float(input('Digite seu peso: '))
r = p / (a ** 2)
if r < 18.5:
    print(f'Abaixo do peso! IMC: {r:.2f}')
elif r >= 18.5 and r < 25:
    print(f'Peso ideal! IMC: {r:.2f}')
elif r >= 25 and r < 30:
    rint(f'Sobrepeso! IMC: {r:.2f}')
elif r >= 30 and r < 40:
    print(f'Obesidade! IMC: {r:.2f}')
else:
    print(f'Obesidade mórbida! IMC: {r:.2f}')



