n = str(input('digite seu nome completo: ')).strip()
print('analisando seu nome...')
print('seu nome em maiuscolos é: {} '.format(n.upper()))
print('seu nome em minusculos é: {} '.format(n.lower()))
print('seu nome tem {} letras '.format(len(n)-n.count(' ')))
print('seu primeiro nome tem {} letras '.format(n.find(' ')))

