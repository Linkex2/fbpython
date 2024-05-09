class Conta:
  def __init__(self, numero, cpf, saldo, ativo=False):
    self.numero = numero
    self.cpf = cpf
    self.saldo = saldo
    self.ativo = ativo

  def ativar():
    if ativo == False:
      print("Ativando Conta...")
      ativo=True
      print("Conta ativada!")
    else:
      print("Conta já está ativa.")

  def debito():
    debito = input("Insira o valor que quer retirar.")
    if saldo - debito > 0:
      saldo = saldo - debito
    else:
      print("Saldo insuficiente.")

  def credito():
    credito = input("Insira o valor que quer adicionar.")
    if credito > 0:
      saldo = saldo + credito
    else:
      print("Insira um valor valido.")