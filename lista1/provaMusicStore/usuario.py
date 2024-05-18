class usuario:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
    
    def criarConta(self):
        self.email = input("Qual o seu email?")
        self.senha = input("Qual a sua senha?")
