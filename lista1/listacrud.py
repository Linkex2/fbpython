import os
os.system("cls")

lista_numeral = list(range(1,11))



def puxa_lista():
    print("-="*5+"[Lista]"+"=-"*5)
    print(lista_numeral)

try:
    escolha = 0
    posicao = 0
    valor = " "

    while True:
        puxa_lista()
        ("Oque você quer fazer na lista?")

        escolha = (int(input("1 - Adicionar um valor na lista\n2 - Exibir lista denovo\n3 - Mudar valor na lista\n4 - Deletar valor da lista\n5 - Sair\nDigite: ")))

        if escolha == 1:
            os.system("cls")
            puxa_lista()
            valor = input("Qual valor você quer adicionar?\nValor: ")
            
            lista_numeral.append(valor)
            valor = " "

            
        elif escolha == 2:
            os.system("cls")
            puxa_lista()
            print("AAAA 2\n")

        elif escolha == 3:
            os.system("cls")
            puxa_lista()
            print("AAAA 3\n")

        elif escolha == 4:
            os.system("cls")
            puxa_lista()
            print("AAAA 4\n")

        elif escolha == 5:
            os.system("cls")
            print("Tchaaaaau o/")
            break
            
        else:
            print("\nValor invalido, tenta denovo")

        
except:
    ...