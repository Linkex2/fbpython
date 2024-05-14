import pymysql
import os
import random

def Cadastro():

    iniciSaldo = 0.00
    op = " "
    escolhaConta = " "
    numero = random.randint(10000,99999)
    print("CADASTRO")
    op=input(f"Bem vindo usuario {numero}\nQual tipo de conta você quer fazer?\n1 - Poupanca \n2 - Corrente \n3 - Empresarial\n4 - Estudantil\n5 - Especial\n6 - Sair\nOpção: ")


    if op == "1":
        escolhaConta = "Poupanca"
        op = " "
        print(f"Conta: {escolhaConta}")
        aniversario=input("Qual o dia do seu aniversario? (01 - 31): ")
    elif op == "2":
        escolhaConta = "Corrente"
        op = " "
        print(f"Conta: {escolhaConta}")
    elif op == "3":
        escolhaConta = "Empresa"
        op = " "
        print(f"Conta: {escolhaConta}")
    elif op == "4":
        escolhaConta = "Estudantil"
        op = " "
        print(f"Conta: {escolhaConta}")
    elif op == "5":
        escolhaConta = "Especial"
        op = " "
        print(f"Conta: {escolhaConta}")
    else:
        os.system("cls")
        print("Valor invalido, tente denovo\n1 - Poupanca \n2 - Corrente \n3 - Empresarial\n4 - Estudantil\n5 - Especial\n6 - Sair\nOpção: ")

    if escolhaConta != " ":
            
        cpf = input("Informe o seu CPF:")
        iniciSaldo = input("Qual o seu saldo inicial?: R$")

        conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='fbradesco',
            database='bancocn'
        )

        cursor = conexao.cursor()

        if escolhaConta == "Poupanca":
            cursor.execute(f"INSERT INTO {escolhaConta} (numero, saldo, aniversario, ativo) values({numero},{iniciSaldo},{aniversario},{False})")
        elif escolhaConta == "Corrente":
            cursor.execute(f"INSERT INTO {escolhaConta} (numero, saldo, contadorTalao, ativo) values({numero},{iniciSaldo},0,{False})")
        elif escolhaConta == "Empresarial":
            cursor.execute(f"INSERT INTO {escolhaConta} (numero, saldo, emprestimoEmpresa, ativo) values({numero},{iniciSaldo},10000,{False})")
        elif escolhaConta == "Estudantil":
            cursor.execute(f"INSERT INTO {escolhaConta} (numero, saldo, limiteEstudantil, ativo) values({numero},{iniciSaldo},5000,{False})")
        elif escolhaConta == "Especial":
            cursor.execute(f"INSERT INTO {escolhaConta} (numero, saldo, limite, ativo) values({numero},{iniciSaldo},1000,{False})")
        else:
            print("Erro, escolhaConta inexistente")
            
        conexao.commit()
            
    else:
        print("Tchaaaau")