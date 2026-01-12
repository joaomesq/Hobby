import datetime

class Conta:

    def __init__(self, numero, titular, saldo, limite = 160000.0):
        self._saldo = saldo
        self._numero = numero
        self._titular = titular
        self._limite = limite
        self._data_abertura = datetime.datetime.today()
        self._transacoes = []
    
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

if __name__ == '__main__':
    conta = Conta(123, "Mesquita", 1000)
    c1 = Conta(12, "Euclides", 200)
    conta.deposita(300)
    conta.transfere_para(c1, 900)
    conta.extrato()