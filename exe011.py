#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessaria para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m quadrados.

l = float(input("Digite a largura da parede: "))
alt = float(input("Digite a altura da parede: "))
print("A área da parede é {:.1f} é necessario {:.1f} litros de tinta!".format(l * alt, l * alt / 2))
