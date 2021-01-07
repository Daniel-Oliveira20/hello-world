def escreva(msg):
    tam = len(msg) + 4
    print("-" * tam)
    print(f" {msg}") 
    print("-" * tam)


c = 0
v = int(input("Digite o numero de mensagens que deseja formatar: "))
while c < v:
    msg = str(input("Digite a mensagem a ser formatada: "))
    escreva(msg)
    c = c + 1
    