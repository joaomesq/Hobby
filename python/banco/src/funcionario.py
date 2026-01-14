class Funcionario:
    def __init__(self, nome, nif, salario):
        self._nome = nome
        self._nif = nif
        self._salario = salario
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        self._nome = valor
    
    @property
    def nif(self):
        return self._nif
    
    @nif.setter
    def nif(self, valor):
        self._nif = valor
    
    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, valor):
        self._salario = valor

    def get_bonifacao(self):
        return self._salario * 0.10

class Gerente(Funcionario):
    def __init__(self, senha, qtd_gerenciaveis, nome, nif, salario):
        super().__init__(nome, nif, salario)
        self._senha = senha
        self._qtd_gerenciaveis = qtd_gerenciaveis
    
    def get_bonifacao(self):
        return super().get_bonifacao() + 1000
    
    
    def __str__(self):
        return '<Classe {}; Endereço {}>'.format(self.__class__.__name__, id(self))

if __name__ == '__main__':
    f = Funcionario("Mesquita", 1, 200)
    g = Gerente(senha = 12345667, qtd_gerenciaveis = 3, nome = "Tista", nif = 1, salario = 3000)
    print(f)
    print(repr(g))
    if(hasattr(g, "get_bonifacao")):
        print("possui o metodo")
    
