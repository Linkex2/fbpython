class Produto:
    def __init__(self, codigo, nome, valor, estoque):
        self.codigo = codigo
        self.nome = nome
        self.valor = valor
        self.estoque = estoque

    def comprar(self):
        opcaoCompra = 'S'
        quantidade = int(input("Quantos produtos você quer comprar?\nQuantidade: "))
        
        while opcaoCompra == 'S':

            if quantidade < 0:
                print("Insira um valor valido!!!\n")
                quantidade = 0

            elif quantidade <= self.estoque:
                self.estoque - quantidade
                quantidade = 0
                opcaoCompra = 'N'
                print("Obrigado por comprar!")
            else:
                quantidade = 0
                opcaoCompra = input("Valor excedente. Deseja continuar? S/N").upper()
                if opcaoCompra != 'S' or 'N':
                    while opcaoCompra != 'S' or 'N':
                        opcaoCompra = input('Escreve direito, deseja continuar? S/N')
            print("Ok!")

    def estocar(self):
        loop = 'S'

        while loop == 'S':
            quantidade = int(input("Quantos estoques chegaram?\nQuantidade: "))
            
            if quantidade < 0:
                print("Insira um valor valido!!!\n")
                quantidade = 0

            else:
                self.estoque + quantidade
                quantidade = 0

                loop = input("Produto adicionado!!!\nQuer adicionar mais? S/N").upper()
                if loop != 'S' or 'N':
                    while loop != 'S' or 'N':
                        loop = input('Escreve direito, deseja continuar? S/N')
        print("Ok!")
