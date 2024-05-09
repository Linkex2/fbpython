from BanquinhoDaSofrencia import Conta
class Poupanca(Conta):
  def __init__(self, numero, saldo, aniversario, ativo = False):
    super().__init__(numero, saldo, ativo)
    self.aniversario = aniversario

  def correcao(self):
    self.aniversario = input("Qual  dia do seu aniversario? (1 - 30): ")
    data = int(input("Qual dia de hoje? (1 - 30): "))
    
    if self.aniversario == data:
      self.saldo + (self.saldo * 0.5)
    else:
      print("Sem correção pra você.")