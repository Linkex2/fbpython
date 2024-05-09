from Classes import *


print("Banco da Coreia do Norte\nNos amamos dinheiro!!!")

PouConta = Poupanca(40324, 0, 21)



tipoConta = 0
tipoConta = int(input("Qual você quer colega?\n1 - Conta Poupança\n2 - Conta Corrente\n3 - Conta Especial\n4 - Conta Empresa\n5 - Conta Estudantil\n6 - Sair\nDigite o numero a opção: "))

if tipoConta == 1:
    print("WooHoo Poupança")
    for x in range(1,10):
        print("Conta Poupança")
        print(f"Saldo atual: {PouConta.saldo}")
        print(f"{x}º Movimento")
        op = " "
        op = input("D - Debito ou C - Credito?").upper()
        if op == "D":
            PouConta.debito()
        elif op == "C":
            PouConta.credito()
        else: 
            print("Movimento perdido.")

elif tipoConta == 2:
    ...
elif tipoConta == 3:
    ...
elif tipoConta == 4:
    ...
elif tipoConta == 5:
    ...
elif tipoConta == 6:
    print("Tchau tchau")
else:
    print("Cai fora, insira um valor valido.")
    