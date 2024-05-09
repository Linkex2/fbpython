from BanquinhoDaSofrencia import Conta
class Especial(Conta):
    def __init__(self, numero, saldo, limite = 1000, ativo = False):
        super().__init__(numero, saldo, ativo)
        self.limite = limite

    def debitoSoQueBom(self):
        debito = input("Insira o valor que quer retirar.")
        
        if self.saldo - debito > 0:
            self.saldo = self.saldo - debito
        else:
            op = " "
            op = input("Saldo insuficiente.\nVocê quer usar o saldo especial? S/N: ").upper()
            if op == "S":
                cortaLimite = input("Quantos você quer?: R$")
                
                if cortaLimite <= self.limite:
                    self.limite - cortaLimite
                    self.saldo = self.saldo + cortaLimite
                    self.saldo = self.saldo - debito
                    print(f"Você retirou R${debito} reais")
                else:
                    print("Limite excedido, cancelando operação.")
            else:
                print("Then get the fuck outta here.")

                
            