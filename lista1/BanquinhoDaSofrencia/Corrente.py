from BanquinhoDaSofrencia import Conta

class Corrente(Conta):
    def __init__(self, numero, saldo, contadorTalao, ativo = False):
        super().__init__(numero, saldo, ativo)
        self.contadorTalao = contadorTalao
  
    def pediTalao(self):
        if self.contadorTalao < 3:
            op = " "
            op = input("Quer pedir um cheque? (S/N): ").upper()

            if op == "S":
                self.contadorTalao = self.contadorTalao + 1
                saldo = saldo - 30
                print("Cheque solicitado!")
            else:
                print("Escreve direito.")

        else:
            print("Ok. Tchaaaau")