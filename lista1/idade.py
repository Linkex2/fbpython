# programa para calcular a idade de uma pessoa
nome = input("Digite o nome da pessoa: ").capitalize
print(f"Olá {nome}, tudo bem?")
anos = int(input("Digite quantos anos você tem: "))
mes = int(input("Que mês é hoje? [1 - 12]: "))
dia = int(input("Que dia é hoje? [1 - 31]: "))

total = (dia) + (mes * 12) + (anos * 365)
print(f"Você viveu {total} dias!!!")

