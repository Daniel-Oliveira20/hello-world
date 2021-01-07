#crie um programa que leia quanto de dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
def converter(r, d):
    c = r / d
    print("Com {} reais você pode comprar {:.2f} dolares! ".format(r, c))


v = "s"
while v == "s":
    r = float(input("Quanto deseja converter? R$ "))
    d = float(input("Quanto está o dólar hoje? "))
    converter(r, d)
    v = str(input("Deseja continuar? s/n: "))

