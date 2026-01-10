from conta import Conta
from cliente import Cliente

cliente = Cliente(nome = "João", sobrenome = "Mesquita", nif = "1234")
conta = Conta(saldo = 1000, cliente = cliente, numero = 123)

conta.depositar(-2456)
conta.historico.imprimir()
