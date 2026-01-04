class Conta:
    def __init__(self, numero, cliente, saldo):
        self.numero = numero
        self.titular = cliente
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if(self.saldo < valor):
            return False

        self.saldo -= valor
        return True
    
    def extrato(self):
        print("Número: {}\nSaldo: {}\n".format(self.numero, self.saldo))
    
    def transfere_para(self, destino, valor):
        if(self.sacar(valor)):
            destino.depositar(valor)
            return True
        else:
            return False