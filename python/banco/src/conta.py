class Conta:

    def __init__(self, numero, titular, saldo, limite = 160000.0):
        self._saldo = saldo
        self._numero = numero
        self._titular = titular
        self._limite = limite
    

if __name__ == '__main__':
    conta = Conta(123, "Mesquita", 1000)
    print(conta._saldo)