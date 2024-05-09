import math

A = int(input("Digite o valor de A: "))
B = int(input("Digite o valor de B: "))
C = int(input("Digite o valor de C: "))

try:
    A = int(a)
    B = int(b)
    C = int(c)
except:
    print("Você digitou um valor errado")

R = (A+B ) ** 2
S = math.pow((B+C), 2.)
D = ((R+S) / 2)

print(f"O resultado de D é {D}")