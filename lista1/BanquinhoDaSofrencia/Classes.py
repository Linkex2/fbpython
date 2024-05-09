class Conta:
  def __init__(self, numero, cpf, saldo, ativo = False):
    self.numero = numero
    self.cpf = cpf
    self.saldo = saldo
    self.ativo = ativo

  def ativar(self):
    if ativo == False:
      print("Ativando Conta...")
      ativo=True
      print("Conta ativada!")
    else:
      print("Conta já está ativa.")

  def debito(self):
    debito = 0
    debito = input("Insira o valor que quer retirar.")
    if self.saldo - self.debito > 0:
      saldo = saldo - debito
      debito = 0
    else:
      print("Saldo insuficiente.")
      debito = 0

  def credito(self):
    credito = input("Insira o valor que quer adicionar.")
    if credito > 0:
      saldo = saldo + credito
    else:
      print("Insira um valor valido.")


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

