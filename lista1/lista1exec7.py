A = int(input("Digite valor A: "))
B = int(input("Digite valor B: "))
C = int(input("Digite valor C: "))
D = int(input("Digite valor D: "))
E = int(input("Digite valor E: "))
F = int(input("Digite valor F: "))


X = ((C * E) - (B * F)) / ((A * E) - (B * D))
Y = ((A * F) - (C * D)) / ((A * E) - (B * D))

print(f"O valor de X é {X}, o valor de Y é {Y}")
