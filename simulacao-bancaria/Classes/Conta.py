from Classes.Extrato import Extrato
import datetime


class Conta:

    def __init__(self, clientes, numero, saldo, banco):
        self.clientes = clientes
        self.__numero = numero
        self.__saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato()
        banco.adicionar_conta(self)
        for cliente in clientes:
            banco.adicionar_cliente(cliente)

    @property
    def numero(self):
        return self.__numero

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            print('Saldo invalido.')
        else:
            self.__saldo = valor

    def depositar(self, valor):
        self.__saldo += valor
        self.extrato.transacoes.append(['DEPOSITO', valor, datetime.datetime.today()])

    def sacar(self, valor):
        if self.__saldo < valor:
            return False
        else:
            self.__saldo -= valor
            self.extrato.transacoes.append(['SAQUE', valor, datetime.datetime.today()])
            return True

    def gerar_saldo(self):
        for cliente in self.clientes:
            print(f'\nnome: {cliente.nome}\nEndereço: {cliente.endereco}')
        print(f'\nNumero da conta: {self.__numero}\nSaldo: {self.__saldo}\n')

    def _atualiza_saldo(self, novo_saldo):
        self.__saldo = novo_saldo

    def transfere_valor(self, conta_destino, valor):
        if self.__saldo < valor:
            return 'não existe saldo suficiente'
        else:
            conta_destino.depositar(valor)
            self.__saldo -= valor
            self.extrato.transacoes.append(['TRANSFERENCIA', valor, datetime.datetime.today()])
            return' transferencia realizada'