from BanquinhoDaSofrencia import Conta
class Estudantil(Conta):
    def __init__(self, numero, saldo, limiteEstudantil = 5000, ativo = False):
        super().__init__(numero, saldo, ativo)
        self.limiteEstudantil = limiteEstudantil

    def usarEstudantil(self):
        if self.limiteEstudantil > 0:
            op = " "
            op = input("Você quer usar o saldo estudantil? (S/N): ").upper()
            if op == "S":
                valor = 0
                valor = input("Quanto você quer retirar?")
                if valor <= self.limiteEstudantil:
                    self.saldo + valor
                    self.limiteEstudantil = self.limiteEstudantil - valor
                    valor = 0
                    op = " "
            
        else:
            print("Limite estudantil zerado, não é possivel usar.")