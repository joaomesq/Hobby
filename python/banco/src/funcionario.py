import abc

class Funcionario(abc.ABC):
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
    
    @abc.abstractmethod
    def get_bonifacao(self):
        pass

class Gerente(Funcionario):
    def __init__(self, senha, qtd_gerenciaveis, nome, nif, salario):
        super().__init__(nome, nif, salario)
        self._senha = senha
        self._qtd_gerenciaveis = qtd_gerenciaveis
    
    def get_bonifacao(self):
        return self._salario * 0.15
    
    
    def __str__(self):
        return '<Classe {}; Endereço {}>'.format(self.__class__.__name__, id(self))

class Diretor(Funcionario):
    def get_bonifacao(self):
        return self._salario * 0.15
        
if __name__ == '__main__':
    g = Gerente(senha = 12345667, qtd_gerenciaveis = 3, nome = "Tista", nif = 1, salario = 3000)
    d = Diretor(nome = "Tista", nif = 12, salario = 2000)
    print(g.get_bonifacao())
    
