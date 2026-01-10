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
    def __init__(self, numero, cliente, saldo):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo
        self.historico = Historico()

    def depositar(self, valor):
        if(valor <= 0):
            print("O valor precisa ser superior a zero")
            return False

        self.saldo += valor
        self.historico.transacoes.append("Deposito de {}".format(valor))
    
    def sacar(self, valor):
        if(self.saldo < valor):
            print("Saldo insuficiente")
            return False

        self.saldo -= valor
        self.historico.transacoes.append("Saque de {}".format(valor))
        return True
    
    def extrato(self):
        print("Número: {}\nSaldo: {}\n".format(self.numero, self.saldo))
        self.historico.transacoes.append("Tirou extrato - saldo de {}".format(self.saldo))
    
    def transfere_para(self, destino, valor):
        if(self.sacar(valor)):
            destino.depositar(valor)
            self.historico.transacoes.append("Transferência de {} para {}".format(valor, destino.numero))
            return True
        else:
            return False