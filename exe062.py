'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais
alguns termos. O programa encerra quando ele disser que quer mostrer 0 termos'''
p = int(input('Primeiro termo: '))
r = int(input('Razão: '))
t = p 
c = 1
v = 10
tot = 0
while v != 0:
    tot += v
    while c <= tot:
        print(t , end=' ')
        t += r
        c += 1
    print('pausa')
    v = int(input('Quantos termos quer mostrar a mais? '))
print(f'Ao total foram {tot} termos.')
