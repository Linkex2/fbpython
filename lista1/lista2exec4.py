import math

numero = int(input("Insira um numero: "))

if numero < 0:
    print("Este numero é Negativo")
elif numero >= 0:
    print("Este numero é Positivo")
else:
    print("Coloque um numero valido")

if numero % 2 == 0:
    print("Numero Par")
else:
    print("Numero Impar")