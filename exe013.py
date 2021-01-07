#faça um algoritmo que leia o salario de um funcionario e mostre o novo salario com um porcentagem definida pelo usiadio
s = float(input("Digite o salario do funcionario R$: "))
a = float(input("Digite a porcentagem do aumento %: "))
print("O salario com {:.0f56}% de aumento passa a ser: {:.2f}".format(a, s+(s*a/100)))
