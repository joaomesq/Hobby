import datetime
import abc
from atualizador_de_conta import AtualizadorDeConta

class Conta(abc.ABC):
    _tipo = None

    def __init__(self, numero, titular, saldo, limite = 160000.0):
        self._saldo = saldo
        self._numero = numero
        self._titular = titular
        self._limite = limite
        self._data_abertura = datetime.datetime.today()
        self._transacoes = []
    
    def __str__(self):
        return "Dados da Conta:\nNúmero {}\nTipo {}\nTitular {}\nSaldo {}\nLimite {}".format(self._numero, type(self)._tipo, self._titular, self._saldo, self._limite)

    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, valor):
        self._numero = valor
    
    @property
    def titular(self):
        return self._titular
    
    @titular.setter
    def titular(self, valor):
        self._titular = valor

    @property
    def limite(self):
        return self._limite
    
    @limite.setter
    def limite(self, valor):
        self._limite = valor

    def saca(self, valor):
        if(valor > self._saldo):
            print("Saldo insuficiente")
            return False
        elif(valor <= 0):
            print("Não pode levantar valores iguais ou menores que zero")
            return False
        
        self._saldo -= valor
        self._transacoes.append("Lenvatou {}".format(valor))
    
    def deposita(self, valor):
        if(valor <= 0):
            print("Valor não permitido")
            return False
        
        self._saldo += valor
        self._transacoes.append("Depositou {}".format(valor))
    
    def transfere_para(self, destino, valor):
        if(valor <= self._saldo and valor > 0):
            if(valor < self._saldo):
                self._saldo -= valor
            destino.deposita(valor)
            self._transacoes.append("Transferiu {} para {}".format(valor, destino.numero))

    
    def extrato(self):
        print("Data de abetura:  {}".format(self._data_abertura))
        for t in self._transacoes:
            print("- {}".format(t))
        
        print("Saldo: {}".format(self._saldo))
    
    @abc.abstractmethod
    def atualiza(self, taxa):
        pass

#ContaCorrente
class ContaCorrente(Conta):

    def __init__(self, saldo, numero, titular):
        super().__init__(numero = numero, titular = titular, saldo = saldo)
        type(self)._tipo = "Conta corrente"

    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 2
        return self._saldo

    def deposita(self, valor):
        super().deposita(valor - 0.10)

#ContaPoupança
class ContaPoupanca(Conta):
    def __init__(self, saldo, numero, titular):
        super().__init__(numero = numero, titular = titular, saldo = saldo)
        type(self)._tipo = "Conta Poupança"
        
    def atualiza(self, taxa):
        self._saldo += self._saldo * taxa * 3
        return self._saldo

class ContaInvestimento(Conta):
    def __init__(self, saldo, numero, titular):
        super().__init__(numero = numero, titular = titular, saldo = saldo)
        type(self)._tipo = "Conta investimento"
        
    def atualiza(self, taxa):
        pass

if __name__ == '__main__':
    cc = ContaCorrente(numero = 2, titular = "Euclides", saldo = 1000)
    cp = ContaPoupanca(numero = 3, titular = "Baptista", saldo = 1000)
    ci = ContaInvestimento(numero = 4, titular = "Mesquita", saldo = 1000)

    ac = AtualizadorDeConta(0.1)

    print(cc)
    print(cp)
    print(ci)