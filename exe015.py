# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por KM rodado.
d = int(input("Quantos dias alugados? "))
km = float(input("Quantos KMrodados? "))
t = (d * 60) + (km * 0.15)
print("Valor total a pagar {:.2f}".format(t))

