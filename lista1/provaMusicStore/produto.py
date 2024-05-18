class produto:
    def __init__(self, descricao, marca, valor = 0.0, estoque = 0):
        self.descricao = descricao
        self.marca = marca
        self.valor = valor
        self.estoque = estoque

    def incluir(self, qtde):
        self.estoque + qtde

    def retirar(self, qtde):
        self.estoque - qtde
    