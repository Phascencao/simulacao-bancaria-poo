from Classes.Conta import Conta
from Classes.Poupança import Poupanca


class ContaRemuneradaPoupanca(Conta, Poupanca):

    def __init__(self, clientes, numero, saldo, banco, taxa_remuneracao):
        Conta.__init__(self, clientes, numero, saldo, banco)
        Poupanca.__init__(self, taxa_remuneracao)

    def remunera_conta(self):
        self.saldo += self.saldo * (self.taxa_remuneracao / 30)
