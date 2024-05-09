try:
    indice = float(input("Digame o indice de poluição"))

    if indice >= 0.3:
        print("Fabrica 1: Pare")
        print("Fabrica 2: Continue")
        print("Fabrica 3: Continue")

    elif indice >= 0.4:
        print("Fabrica 1: Pare")
        print("Fabrica 2: Pare")
        print("Fabrica 3: Continue")
    elif indice >= 0.4:
        print("Fabrica 1: Pare")
        print("Fabrica 2: Pare")
        print("Fabrica 3: Pare")
    else:
        print("Indice não excedido, continuem assim")

except:
    print("Insira um valor valido")