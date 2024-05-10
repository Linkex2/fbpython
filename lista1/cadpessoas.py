import pymysql
import os

def limpatela():
    os.system('cls')

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='fbradesco',
    database='agenda'
)

cursor = conexao.cursor()

cursor.execute("SELECT * FROM usuarios")

resultados = cursor.fetchall()
print(resultados)

#dados = ("Maria Aparecida","ma@gmail.com","11 98888-8888","Exemplo usando inserção no Python")

#cursor.execute("INSERT INTO usuarios (nome, email, telefone, mensagem) values(%s,%s,%s,%s)", dados)

conexao.commit()

cursor.execute("SELECT * FROM usuarios")

resultados = cursor.fetchall()
print(resultados)

conexao.close()