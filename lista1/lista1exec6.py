import math

x1 = int(input("Valor x1: "))
x2 = int(input("Valor x2: "))
y1 = int(input("Valor y1: "))
y2 = int(input("Valor y2: "))

d = math.sqrt(math.pow((x2 - x1),2) + math.pow((y2 - y1),2))

print(f"O resultado é: {int(d)}")
