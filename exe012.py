#faça um algoritmo que leia o preço de um produto e mostre seu novo preço com desconto digitado pelo usuário.

v = float(input("Digite o valor do produto: "))
d = float(input("Digite o valor do desconto: "))
print("Ovalor do produto com desconto é: {:.2f}".format(v -(v * d / 100)))
