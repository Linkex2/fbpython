import math

num1 = int(input("Insira o numero 1: "))
num2 = int(input("Insira o numero 2: "))
num3 = int(input("Insira o numero 3: "))

if num3 >= 1000:
    print(f"Numero 3 é {math.pow((num3),2)}")

else:
    num4 = int(input("Insira o numero 4: "))
    print(f"Numero 1 é {int(math.pow((num1),2))}\nNumero 2 é: {int(math.pow((num2),2))}\nNumero 3 é: {int(math.pow((num3),2))}\nNumero 4 é: {int(math.pow((num4),2))}")
