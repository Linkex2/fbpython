from BanquinhoDaSofrencia import Conta
class Empresa(Conta):
    def __init__(self, numero, saldo, emprestimoEmpresa = 10000, ativo = False):
        super().__init__(numero, saldo, ativo)
        self.emprestimoEmpresa = emprestimoEmpresa

    def pedirEmprestimo(self):
        if self.emprestimoEmpresa > 0:
             
            op = " "
            op = input("Quer pedir emprestimo? (S/N):").upper
            if op == "S":
                valor = input("Quantos você quer?: R$")

                if valor <= self.emprestimoEmpresa:
                    self.saldo = self.saldo + valor
                    self.emprestimoEmpresa = self.emprestimoEmpresa - valor
                    valor = 0
                    op = " "
                
                else:
                        print("Valor excede o limite do emprestimo.")
        else:
            print("Emprestimo zerado, impossivel pedir")
                


