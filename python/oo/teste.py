from conta import Conta
from cliente import Cliente

cliente = Cliente(nome = "João", sobrenome = "Mesquita", nif = "1234")
conta = Conta(saldo = 1000, cliente = cliente, numero = 123)

conta.depositar(100)
conta._numero = 29
conta.numero = 90
print(conta._numero)
conta._historico.imprimir()

class Pessoa:
    _total_pessoas = 0

    __slots__ = ['_nome', '__idade']

    def __init__(self, nome, idade):
        self.__idade = idade
        self._nome = nome
        type(self)._total_pessoas += 1

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, valor):
        if(valor <= 0):
            print("Idade não pode ser menor ou igual a zero")
            return False
        else:
            self.__idade = valor
    
    @classmethod
    def get_total_pessoas(cls):
        return cls._total_pessoas