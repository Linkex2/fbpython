import pymysql
import os
import time
from cadastroUsuario import *
from produto import *
from movimento import *

def cabecalho():
    print("-="*10+"- ","MusicStore","-="*10+"-")

def esperar():
    time.sleep(1)
    print(". ", end='')
    time.sleep(1)
    print(". ", end='')
    time.sleep(1)
    print(".")
def esperarRapido():
    print(". . .")
    time.sleep(2)
    os.system("cls")

    

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='fbradesco',
    database='musicstore',
)

cursor = conexao.cursor()

cabecalho()

loop = 'S'
while loop == 'S':
    op = input("Oque você quer fazer?\n1 - Criar Produto\n2 - Listar Produtos\n3 - Alterar Produto\n4 - Deletar Produto\n5 - Cadastrar Usuario\n6 - Movimentar\n7 - Sair\nOpção: ")
    if op == '1':

        descricao = input("Qual o nome do produto?\nNome: ")
        marca = input("Qual a marca do produto?\nMarca: ")
        valor = float(input('Qual o preço do produto?\nValor: R$'))
        estoque = int(input('Quantos deste produto temos no estoque?\nEstoque: '))
        while estoque <= 0 or estoque > 37:

            if estoque <= 0:
                estoque = int(input("Valor negativo ou zerado.\nInsira um valor valido!!!\nValor: "))
            elif estoque > 37:
                estoque = int(input("Valor excede nosso estoque.\nInsira um igual ou menor que 37\nValor: "))
            else:
                break
        
        criaProduto = produto(descricao,marca,valor,estoque)


        insert = "INSERT INTO produtomusica (descricao, marca, valor, estoque) VALUES (%s, %s, %s, %s)"
        cursor.execute(insert, (criaProduto.descricao, criaProduto.marca, criaProduto.valor, criaProduto.estoque))
        conexao.commit()

        esperar()
        read = "SELECT * FROM produtomusica WHERE descricao = %s"
        cursor.execute(read, (criaProduto.descricao))
        printProduto = cursor.fetchall()

        print("Produto adicionado com sucesso!!!\n")
        print(printProduto)
        esperarRapido()


    elif op == '2':
        read = "Select * From produtomusica"
        cursor.execute(read)
        readResultado = cursor.fetchall()
        print(readResultado)

    elif op == '3':

        idUpdate = input("Qual ID do Produto?\nID: ")

        read = "SELECT * FROM produtomusica WHERE id_produtomusica = %s"
        cursor.execute(read, (idUpdate))
        printProduto = cursor.fetchall()
        print(f"Produto atual: {printProduto}")

        descricao = input("Qual o nome do produto?\nNome: ")
        marca = input("Qual a marca do produto?\nMarca: ")
        valor = float(input('Qual o preço do produto?\nValor: R$'))
        estoque = int(input('Quantos deste produto temos no estoque?\nEstoque: '))
        while estoque <= 0 or estoque > 37:

            if estoque <= 0:
                estoque = int(input("Valor negativo ou zerado.\nInsira um valor valido!!!\nValor: "))
            elif estoque > 37:
                estoque = int(input("Valor excede nosso estoque.\nInsira um igual ou menor que 37\nValor: "))
            else:
                break
        
        updateProduto = produto(descricao,marca,valor,estoque)


        update = "UPDATE produtomusica SET descricao = %s, marca = %s, valor = %s, estoque = %s WHERE id_produtomusica = %s"
        cursor.execute(update, (updateProduto.descricao, updateProduto.marca, updateProduto.valor, updateProduto.estoque, idUpdate))
        conexao.commit()

        esperar()
        read = "SELECT * FROM produtomusica WHERE id_produtomusica = %s"
        cursor.execute(read, (idUpdate))
        printProduto = cursor.fetchall()
        
        print("Produto atualizado com sucesso!!!\n")
        print(printProduto)
        esperarRapido()

    elif op == '4':

        idDelete = input("Qual ID do Produto?\nID: ")

        read = "SELECT * FROM produtomusica WHERE id_produtomusica = %s"
        cursor.execute(read, (idDelete))
        printProduto = cursor.fetchall()
        print(f"Produto atual: {printProduto}")

        escolha = input("Tem certeza que quer deletar esse produto? S/N\n Resposta: ")
        while escolha != 'S' or escolha != 'N':

            if escolha == 'S':
                print("Confirmado, deletando produto...")

                delete = "DELETE FROM produtomusica WHERE id_produtomusica = %s"
                cursor.execute(delete, (idDelete))
                conexao.commit()

                esperar()
                read = "SELECT * FROM produtomusica"
                cursor.execute(read)
                printProduto = cursor.fetchall()
                
                print("Produto deletado sucesso :(\n")
                esperarRapido()
                print(printProduto)
                break
            elif escolha == 'N':
                print("Cancelando processo de deleção")
                break
            else:
                escolha = input("Resposta errada.\nTem certeza que quer deletar esse produto? S/N\nResposta: ")
        

    elif op == '5':
        cadastro()
    elif op == '6':
        movimento()
    elif op == '7':
        os.system('cls')
        print("Goodbye!\n")
        time.sleep(3)
        break
    else:
        print("Escreve direito!!!\n")
        time.sleep(5)
        os.system('cls')