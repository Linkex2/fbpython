class Cliente: #Classes no Python não precisam usar de construtores completos para serem usados.

    def __init__(self, nome, cpf): #self é o sistema de Super do Java, atributos atribuidos a essa classe
        self.nome = nome #self aqui é o equivalente do this no Java.
        self.cpf = cpf