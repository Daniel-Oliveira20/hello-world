c = "s"
while c == "s":
    a = int(input("Quer contar de quanto: ")) 
    b = int(input("Até quanto: "))
    if a < b:
        while a <= b:
            print(a)
            a = a+1
    elif a > b:
        while a >= b:
            print(a)
            a = a-1
    else:
        print("NUMEROS IGUAIS")
    c = str(input("Deseja continuar? S/N: "))

