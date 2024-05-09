P = int(input("Insira o peso dos tomates Joãozão: "))

if P > 50:

    E = P - 50

    M = E * 4

    print(f"Burro, passou uns {E} kilos, tomou R$ {M}.00 de multa")

else:
    print("Não tomou multa")