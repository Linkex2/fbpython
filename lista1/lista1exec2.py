nome = input("Digite o nome da pessoa: ")
print(f"Olá {nome}, tudo bem?")
dias = int(input("Digite quantos dias você viveu?: "))


anos = (dias // 365)
mes = int((dias % 365) / 30)
dia = (dias % 365) % 30

print(f"Você viveu {dia} dias, {mes} meses e {anos} anos!")