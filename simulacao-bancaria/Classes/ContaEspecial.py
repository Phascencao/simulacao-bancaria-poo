from Classes.Conta import Conta
from datetime import datetime


class ContaEspecial(Conta):

    def __init__(self, clientes, numero, saldo, limite, banco):
        super().__init__([clientes], numero, saldo, banco)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            return False
        else:
            novo_saldo = self.saldo - valor
            self._atualiza_saldo(novo_saldo)
            if (self.saldo < 0):
                self.limite += self.saldo
            self.extrato.transacoes.append(['SAQUE', valor, datetime.today()])
            return True