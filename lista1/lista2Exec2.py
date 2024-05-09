C = input("Digite o codigo do funcionario: ")
N = int(input("Digite o numero de horas trabalhadas: "))

salario = N * 10

if N > 50:
    E = (N - 50) * 20
else:
    E = 0

print(f"Trabalhador: {C}\n Horas totais trabalhadas: {N}\nSalario á pagar: R$ {salario}\n Salario bonus: R$ {E}")