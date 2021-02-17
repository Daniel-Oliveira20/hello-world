v = []
vp = []
vi = []

while True:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        vp.append(n)
    else:
        vi.append(n)
    r = str(input('Quer continuar? S/N ')).strip().upper()[0]
    while r not in 'S/N':
        r = str(input('Quer continuar? S/N ')).upper()
    if r == "N":
        break
print(f'A lista completa dos valores é: {v}')
print(f'A lista só com numeros pares é: {vp}')
print(f'A lista só com numeros impares é: {vi}') 
