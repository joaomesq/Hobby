import datetime
from atualizador_de_conta import AtualizadorDeConta

class Conta:

    def __init__(self, numero, titular, saldo, limite = 160000.0):
        self._saldo = saldo
        self._numero = numero
        self._titular = titular
        self._limite = limite
        self._data_abertura = datetime.datetime.today()
        self._transacoes = []
    
    def __str__(self):
        return "Dados da Conta:\nNúmero {}\nTitular {}\nSaldo {}\nLimite {}".format(self._numero, self._titular, self._saldo, self._limite)

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
    
    def atualiza(self, taxa):
        self._saldo =+ self._saldo * taxa
        return self._saldo

#ContaCorrente
class ContaCorrente(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * 2 * taxa
        return self._saldo

    def deposita(self, valor):
        super().deposita(valor - 0.10)

#ContaPoupança
class ContaPoupanca(Conta):
    def atualiza(self, taxa):
        self._saldo += self._saldo * 3 * taxa
        return self._saldo


if __name__ == '__main__':
    conta = Conta(123, "Mesquita", 1000)
    cc = ContaCorrente(numero = 2, titular = "Euclides", saldo = 1000)
    cp = ContaPoupanca(numero = 3, titular = "Baptista", saldo = 1000)
    
    ac = AtualizadorDeConta(0.1)

    ac.roda(cc)
    ac.roda(conta)
    ac.roda(cp)