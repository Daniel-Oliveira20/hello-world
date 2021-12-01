'''Crie um programa que leia nome sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista. No final, mostre:
A Quantas pessoas foram cadastradas.
B A méria de idade das pessoas.
C As mulheres cadastradas.
D As pessoas acima da média de idade.'''
lista = []
pessoa = {}
mi = s = 0
print('=-' * 20)
print('----CADASTRANDO PESSOAS----')
print('=-' * 20)
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo M/F ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('M para masculino ou F para feminino')
    pessoa['idade'] = int(input('Idade: '))
    s += pessoa['idade']
    lista.append(pessoa.copy())
    opc = str(input('Quer continuar? S/N ')).upper()[0]
    if opc == 'N': 
        break
    while opc != 'S' and opc != 'N':
        print('S para sim ou N para não')
        opc = str(input('Quer continuar? S/N ')).upper()[0]
mi = s / len(lista)
print('')
print('RESULTADO')
print('-' * 20)
print(f'Foram cadastradas {len(lista)} pessoas')
print(f'A média de idade é {mi}')
print('As mulheres cadastradas foram:', end=' ')
for i in lista:
    if i['sexo'] in 'fF':
        print(f'{i["nome"]}', end=' ')
print()
print('Lista de pessoas acima da média de idade:', end=' ')
for i in lista:
    if i['idade'] >= mi:
        print(f'{i["nome"]}', end=' ')
