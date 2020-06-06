verif = "s"
contm = 0
contf = 0
while verif != "n":
    sexo = str(input("Qaul é o sexo? M/F: "))
    idade = int(input("Digite a idade: "))
    print("Qual é a cor do cabelo? ")
    print("{1} preto")
    print("{2} castanho")
    print("{3} loiro")
    print("{4} ruivo")
    cabelo = int(input())
    if sexo == "m" and idade >= 18 and cabelo == 2:
        contm = contm + 1
    elif sexo == "f" and idade >= 18 and cabelo == 4:
        contf = contf + 1
    verif = str(input("quer continuar? S/N: "))
print("O número de homens com cabelos castanhos maior de idade é: ", contm )
print("O número de mulheres com cabelos ruivos maior de idade é: ", contf )

