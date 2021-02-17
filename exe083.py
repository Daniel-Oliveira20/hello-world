'''Crie um programa onde o usuário digite uma expressão qualquer 
que use parẽnteses. Seu aplicativo deverá analisar se a expressão passada
está com parênteses abertos e fechados na ordem correta.'''
exp = str(input('Digite a expressão: '))
pilha = []
for s in exp: 
    if s == '(':
        pilha.append('(')
    elif s == ')':
        if len(pilha) > 0:
            pilha.pop
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão valida!')
else:
    print('Expressão INVALIDA!')
