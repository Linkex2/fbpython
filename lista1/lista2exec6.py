try:

    idade = int(input("Insira uma idade valida: "))
    if idade < 5:
        print("Bebe, não permitido na piscina.")
    elif idade <= 7:
        print("Infantil A")
    elif idade <= 11: 
        print("Infantil B")
    elif idade <= 13:
        print("Juvenil A")
    elif idade <= 17:
        print("Juvenil B")
    elif idade >= 18:
        print("Adulto")
    else:
        print("Feto detectado!!!/n Aborto iminente!")

except:
    print("Insira uma idade valida")