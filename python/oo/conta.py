import datetime

class Historico:
    def __init__(self):
        self.data_abertura = datetime.datetime.today()
        self.transacoes = []

    def imprimir(self):
        print("Data abertura: {}".format(self.data_abertura))
        for t in self.transacoes:
            print(" - {}".format(t))


class Conta:

    identificador = 1

    __slots__ = ['_numero', '_titular', '_saldo', '_limite', '_historico']

    def __init__(self, numero, cliente, saldo, limite = 160000.00):
        self._numero = numero
        self._titular = cliente
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        self._identificador = Conta.identificador
        Conta.identificador += 1
    
    @property
    def limite(self):
        return self._titular

    @limite.setter
    def limite(self, valor):
        self._limite = valor
    
    @property
    def numero(self):
        return self._numero
    
    @numero.setter
    def numero(self, valor):
        self._numero = valor
    
    def get_titular(self):
        return self._titular

    def depositar(self, valor):
        if(valor <= 0):
            print("O valor precisa ser superior a zero")
            return False

        self._saldo += valor
        self._historico.transacoes.append("Deposito de {}".format(valor))
    
    def sacar(self, valor):
        if(self._saldo < valor):
            print("Saldo insuficiente")
            return False

        self._saldo -= valor
        self._historico.transacoes.append("Saque de {}".format(valor))
        return True
    
    def extrato(self):
        print("Número: {}\nSaldo: {}\n".format(self._numero, self._saldo))
        self._historico.transacoes.append("Tirou extrato - saldo de {}".format(self._saldo))
    
    def transfere_para(self, destino, valor):
        if(self.sacar(valor)):
            destino.depositar(valor)
            self._historico.transacoes.append("Transferência de {} para {}".format(valor, destino._numero))
            return True
        else:
            return False