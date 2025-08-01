class Banco:

    def __init__(self, nome):
        self.nome = nome
        self.__contas = []
        self.__clientes = []

    def adicionar_conta(self, conta):
        self.__contas.append(conta)

    def adicionar_cliente(self, cliente):
        self.__clientes.append(cliente)

    def listar_contas(self):
        print(f'Contas do banco {self.nome}')
        for conta in self.__contas:
            print(f'Conta Nº: {conta.numero} | Saldo: {conta.saldo:.2f}')

    def listar_clientes(self):
        print(f'Clientes do banco {self.nome}')
        for cliente in self.__clientes:
            print(f'CLiente {cliente.nome} | CPF: {cliente.cpf}')