class AtualizadorDeConta:
    def __init__(self, selic, saldo_total = 0.0):
        self._selic = selic
        self._saldo_total = saldo_total

    @property
    def selic(self):
        return self._selic
    
    @property
    def saldo_total(self):
        return self._saldo_total

    def roda(self, conta):
        print("Saldo da conta: {}".format(conta._saldo))
        self._saldo_total += conta.atualiza(self._selic)
        print("Saldo final da conta: {}".format(self.saldo_total))