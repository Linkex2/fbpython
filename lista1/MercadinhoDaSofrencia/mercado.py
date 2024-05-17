import pymysql
import os
import time
from produto import *

def esperar():
    time.sleep(1)
    print(". ")
    time.sleep(1)
    print(". ")
    time.sleep(1)
    print(".")

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='fbradesco',
    database='DBLoja'
)

cursor = conexao.cursor()

print("Bem Vindo!")

loop = 'S'
while loop == 'S':
    op = input("Oque você quer fazer nesse mercado?\n1 - Criar Produto\n2 - Listar Produtos\n3 - Alterar Produto\n4 - Deletar Produtos\n5 - Comprar Produto\n6 - Sair\nResposta: ")
    if op == '1':
        codigo = input("Qual o codigo desse produto?\nCodigo: ")
        nome = input("Qual o nome do produto?\nNome: ")
        valor = input('Qual o preço do produto?\nPreço: ')
        estoque = input('Quantos deste produto tem no estoque?\nQuantidade: ')

        item = Produto(codigo, nome, valor, estoque)
        cursor.execute(f"INSERT INTO Produto (Codigo, Nome, Valor, Estoque) values ({item.codigo},{item.nome},{item.valor},{item.estoque})")
        conexao.commit()

        esperar()
        cursor.execute(f"Select * From produto Where codigo = {item.codigo}")
        printProduto = cursor.fetchall()
        print("Produto adicionado com sucesso!!!\n")
        print(printProduto)


    elif op == '2':
        cursor.execute("Select * From produto")
        estoqueDB = cursor.fetchall()
        print(estoqueDB)

    elif op == '3':
        ...
    elif op == '4':
        ...
    elif op == '5':
        ...
    elif op == '6':
        os.system('cls')
        print("Goodbye!\n")
        time.sleep(3)
        break
    else:
        print("Escreve direito!!!\n")
        time.sleep(5)
        os.system('cls')