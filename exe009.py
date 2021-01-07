from time import sleep
def vezes(n):
    c = 1
    for c in range (1, 10+1):
        print("{} x {} = {}".format(n, c, n*c))
        sleep(0.5)


def escreve():
    print("-" * 13)


n = int(input("Digite um numero: "))
escreve()
vezes(n)
escreve()




