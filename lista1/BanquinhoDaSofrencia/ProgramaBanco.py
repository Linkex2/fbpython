from Classes import *
from Cadastro import *
import pymysql

conexao = pymysql.connect(
            host='localhost',
            user='root',
            password='fbradesco',
            database='bancocn'
        )

cursor = conexao.cursor()

import os
import time


print("Banco da Coreia do Norte\nNos amamos dinheiro!!!")

PouConta = Poupanca(None, 0.0, None, None)
CorreConta = Corrente(None, 0.0, 0, None)
EmpresaConta = Empresa(None, 0.0, 10000, None)
EstudaConta = Estudantil(None, 0.0, 5000, None)
EspeciConta = Especial(None, 0.0, 1000, None)


tipoConta = 0
tipoConta = int(input("Qual você quer colega?\n1 - Conta Poupança\n2 - Conta Corrente\n3 - Conta Especial\n4 - Conta Empresa\n5 - Conta Estudantil\n6 - Criar Conta\n7 - Sair\nDigite o numero a opção: "))

if tipoConta == 1:
    print("WooHoo Poupança")
    tipoConta = 0

    numConta = int(input("Informe o numero da sua conta.\nSeu Numero: "))
    cursor.execute(f"Select * From poupanca Where numero = {numConta}")
    resposta = cursor.fetchall()
    PouConta = Poupanca(resposta[0][1],resposta[0][4],resposta[0][3],resposta[0][2])
    
    if len(resposta) > 0:

        print(f"Bem vindo usuario nº{PouConta.numero}")

        for x in range(1,10):
            print("Conta Poupança")
            print(f"Saldo atual: {PouConta.saldo}")
            print(f"{x}º Movimento")
            op = " "
            op = input("D - Debito\nC - Credito\n Opção: ").upper()
            if op == "D":
                PouConta.debito()
            elif op == "C":
                PouConta.credito()
            elif op == "S":
                print("Saindo...")
                cursor.execute(f"Update poupanca Set saldo = {PouConta.saldo} Where numero = {numConta}")
                conexao.commit()
                break
            else: 
                print("Movimento perdido.")
            cursor.execute(f"Update poupanca Set saldo = {PouConta.saldo} Where numero = {numConta}")
            conexao.commit()

        print("Obrigado por usar o nosso banco!")
    else:
        print("Não achei sua conta...")

elif tipoConta == 2:
    print("WooHoo Corrente")
    tipoConta = 0

    numConta = int(input("Informe o numero da sua conta.\nSeu Numero: "))
    cursor.execute(f"Select * From corrente Where numero = {numConta}")

    resposta = cursor.fetchall()
    CorreConta = Corrente(resposta[0][1],resposta[0][4],resposta[0][3],resposta[0][2])
    
    for x in range(1,10):

        print("Conta Corrente")
        print(f"Saldo atual: {CorreConta.saldo}")
        print(f"{x}º Movimento")
        op = " "
        op = input("D - Debito\nC - Credito\nT - Pedir Talao\nS - Sair\nOpção: ").upper()
        if op == "D":
            CorreConta.debito()
        elif op == "C":
            CorreConta.credito()
        elif op == "T":
            CorreConta.pediTalao()
        elif op == "S":
            print("Saindo...")
            cursor.execute(f"Update corrente Set saldo = {CorreConta.saldo} Where numero = {numConta}")
            cursor.execute(f"Update corrente Set contadorTalao = {CorreConta.contadorTalao} Where numero = {numConta}")
            conexao.commit()
            break
        else: 
            print("Movimento perdido.")
        cursor.execute(f"Update corrente Set saldo = {CorreConta.saldo} Where numero = {numConta}")
        cursor.execute(f"Update corrente Set contadorTalao = {CorreConta.contadorTalao} Where numero = {numConta}")
        conexao.commit()
    print("Obrigado por usar o nosso banco!")

elif tipoConta == 3:

    print("WooHoo Empresa")
    tipoConta = 0

    numConta = int(input("Informe o numero da sua conta.\nSeu Numero: "))
    cursor.execute(f"Select * From empresa Where numero = {numConta}")

    resposta = cursor.fetchall()
    EmpresaConta = Empresa(resposta[0][1],resposta[0][4],resposta[0][3],resposta[0][2])
    
    for x in range(1,10):
        print("Conta Empresarial")
        print(f"Saldo atual: {EmpresaConta.saldo}")
        print(f"{x}º Movimento")
        op = " "
        op = input("D - Debito\nC - Credito\nE - Pedir Emprestimo\nS - Sair\nOpção: ").upper()
        if op == "D":
            EmpresaConta.debito()
        elif op == "C":
            EmpresaConta.credito()
        elif op == "E":
            EmpresaConta.pedirEmprestimo()
        elif op == "S":
            print("Saindo...")
            cursor.execute(f"Update empresa Set saldo = {EmpresaConta.saldo} Where numero = {numConta}")
            cursor.execute(f"Update empresa Set contadorTalao = {EmpresaConta.emprestimoEmpresa} Where numero = {numConta}")
            conexao.commit()
            break
        else: 
            print("Movimento perdido.")
        cursor.execute(f"Update empresa Set saldo = {EmpresaConta.saldo} Where numero = {numConta}")
        cursor.execute(f"Update empresa Set contadorTalao = {EmpresaConta.emprestimoEmpresa} Where numero = {numConta}")
        conexao.commit()
    print("Obrigado por usar o nosso banco!")

elif tipoConta == 4:
    tipoConta = 0
    print("WooHoo Estudante")
    numConta = int(input("Informe o numero da sua conta.\nSeu Numero: "))
    cursor.execute(f"Select * From estudantil Where numero = {numConta}")

    resposta = cursor.fetchall()
    EstudaConta = Estudantil(resposta[0][1],resposta[0][4],resposta[0][3],resposta[0][2])
    
    for x in range(1,10):
        print("Conta Estudantil")
        print(f"Saldo atual: {EstudaConta.saldo}")
        print(f"{x}º Movimento")
        op = " "
        op = input("D - Debito\nC - Credito\nE - Emprestimo Estudantil\nS - Sair\nOpção: ").upper()
        if op == "D":
            EstudaConta.debito()
        elif op == "C":
            EstudaConta.credito()
        elif op == "E":
            EstudaConta.usarEstudantil()
        elif op == "S":
            print("Saindo...")
            break
        else: 
            print("Movimento perdido.")
    print("Obrigado por usar o nosso banco!")

elif tipoConta == 5:
    print("WooHoo Especial")
    tipoConta = 0
    for x in range(1,10):
        print("Você é especial <3")
        print(f"Saldo atual: {EmpresaConta.saldo}")
        print(f"{x}º Movimento")
        op = " "
        op = input("D - Debito\nC - Credito\nT - Pedir Talao\nS - Sair\nOpção: ").upper()
        if op == "D":
            EmpresaConta.debito()
        elif op == "C":
            EmpresaConta.credito()
        elif op == "T":
            EmpresaConta.pedirEmprestimo()
        elif op == "S":
            print("Saindo...")
            break
        else: 
            print("Movimento perdido.")
        time.sleep(5)
        os.system('cls')
    print("Obrigado por usar o nosso banco!")
elif tipoConta == 6:
    tipoConta = 0
    Cadastro()

elif tipoConta == 7:
    print("Tchau tchau")
    tipoConta = 0
else:
    print("Cai fora, insira um valor valido.")
    