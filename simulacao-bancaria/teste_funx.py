from Classes.Cliente import Cliente
from Classes.Conta import Conta
from Classes.Banco import Banco
from Classes.ContaEspecial import ContaEspecial
from Classes.ContaRemuneradaPoupanca import ContaRemuneradaPoupanca

#testando o codigo
banco = Banco('ITAU')

#criando clientes
cliente1 = Cliente('52421540801', 'Pedro Henrique', 'Rua Gravata, 265')
cliente2 = Cliente('54184161301', 'Julia Benicio', 'Rua agave dragao, 61')
cliente3 = Cliente('99999999999', 'Alan', 'Rua x')
cliente4 = Cliente('88888888888', 'Beatriz', 'Rua y')
cliente5 = Cliente('12345678901', 'joao', 'avenida sla')
cliente6 = Cliente('11111111111', 'AAAAAAAAA', 'rua 1234')
#criando contas
conta1 = Conta([cliente1, cliente2], 111, 0, banco)
conta2 = Conta([cliente3, cliente4], 222, 1000, banco)
conta3 = ContaEspecial(cliente5, 3, 2000, 1000, banco)
conta4 = ContaRemuneradaPoupanca([cliente6], 555, 2000, banco, 0.1)

conta2.depositar(5000)
conta2.transfere_valor(conta3, 2000)
conta1.depositar(10000)
conta1.transfere_valor(conta2, 5000)
conta1.sacar(500)
conta3.sacar(2001)
conta4.remunera_conta()

conta1.extrato.gerar_extrato(conta1)
conta3.extrato.gerar_extrato(conta3)
conta2.extrato.gerar_extrato(conta2)
conta3.gerar_saldo()
conta2.gerar_saldo()
conta1.gerar_saldo()
conta4.gerar_saldo()