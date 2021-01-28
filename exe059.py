'''Crie um programa que leia dios valores e mostre um menu na tela
1 somar
2 multiplicar
3 maior
4 novos números
5 sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
def menu():
    print('--------MENU--------')
    print('=' * 20)
    print('''[1] somar\n[2] multiplicar\n[3] maior\n[4] novos números\n[5] sair do programa''')
    print('=' * 20)


opc = 0
while opc != 5:
    n1 = int(input('Digite um número inteiro: '))
    n2 = int(input('Digite outro número inteiro: '))
    menu()
    opc = int(input('Escolha uma opção: '))
    if opc == 1:
        print(f'A soma entre {n1} e {n2} é: {n1+n2}')
    elif opc == 2:
        print(f'A multiplicação de {n1}x{n2} é: {n1*n2}')
    elif opc == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n2 > n1:
            print(f'{n2} é maior que {n1}')
        else:
            print('NÚMEROS IGUAIS!')
    elif opc == 4:
        n1 = int(input('Digite um número inteiro: '))
        n2 = int(input('Digite outro número inteiro: '))
        menu()
        opc = int(input('Escolha uma opção: '))
    elif opc == 5:
        print('PROGRAMA ENCERRADO')
    else:
        print('OPÇÃO INVALIDA')
