from collections import UserDict

class Pins(UserDict):
    def __contains__(self, key):
        return str(key) in self.keys()
    
    def __setitem__(self, key, value):
        self.data[str(key)] = value

if __name__ == '__main__':
    pinos = Pins(one = 1)
    print(pinos)
    pinos[3] = 1
    lista = [1, 2, 3]
    pinos[lista] = 2
    print(pinos)
    print(pinos['3'])

    from collections import Counter, deque, namedtuple
    cores = ["vermelho", "amarelo", "vermelho", "tista", "Mesquita", "Mesquita", "azul", "verde", "azul", "verde"]
    contador = Counter(cores)
    print(contador)

    fila = deque()
    fila.append("Tista")
    fila.append(contador)
    fila.appendleft(pinos)
    print(fila)

    Conta = namedtuple("Conta", "numero titular saldo")
    conta = Conta(12, "Mesquita", 1000)
    print(conta)
    print(conta.titular)
    print(conta[0])