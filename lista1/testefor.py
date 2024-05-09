import os
os.system('cls')
lista_louca = [123,1,2,3,'MARIA',['PEDRO','PAULO', 3000]] #Lista em Python

lista_louca[0] = 456
lista_louca[5][2] = 6000
lista_louca[5][1][1]

ex1 = ("a",1,"alvo",1,1,"A","a") #Tupla Python
ex1 = set() #set é uma lista que exclui repetiçoes, porem é imutavel.

ex2 = {"a",1,"A",1,1,"a"}

db = {"nome": "PEDRO",
    "idade": 15,
    "Endereço": "Rua Sei Lá, 1000"} #Dicionario Python, literalmente um arquivo JSON.

print(db["Endereço"])