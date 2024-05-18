import pymysql
import os
from usuario import *

def cadastro():

    print("CADASTRO\n")
    criarEmail = input("Email: ")
    criarSenha = input("Senha: ")
    criarUsuario = usuario(criarEmail, criarSenha)



    conexao = pymysql.connect(
        host='localhost',
        user='root',
        password='fbradesco',
        database='musicstore'
    )

    cursor = conexao.cursor()

    insert = "INSERT INTO usuario (email, senha) VALUES (%s, %s)"
    cursor.execute(insert, (criarUsuario.email, criarUsuario.senha))
    
    conexao.commit()