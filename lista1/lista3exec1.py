salario = 0.0
mario_salario = 0.0
total_salario = 0.0
percentual = 0.0
filho = 0
total_filhos = 0

pessoas = int(input("Com quantas pessoas estamos trabalhando?"))
for x in range(pessoas):

    salario = float(input(f"Residente {1+x}\nInsira seu salario: R$"))
        
    if salario > mario_salario:
            mario_salario = salario

    if salario <= 1000:
            percentual = percentual + 1

    total_salario = salario + total_salario

    filho = int(input("Quantos filhos você tem?: "))
    total_filhos = filho + total_filhos

    if x >= pessoas:
        continue

print(f"A media salario é de: R${round(total_salario / 3,2)}")
print(f"O maior salario foi de: R${mario_salario}")
print(f"O percentual de salarios abaixo de R$1000 é de: {round(percentual / 3 * 100,2)}%")
print(f"A media de filhos é: {round(total_filhos / 3,0)}")