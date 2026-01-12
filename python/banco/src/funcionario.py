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

class Gerente(Funcionario):
    def __init__(self, senha, qtd_funcionarios, nome, nif, salario):
        super().__init__(nome, nif, salario)
        self._senha = senha
        self._qtd_funcionarios = qtd_funcionarios

if __name__ == '__main__':
    f = Funcionario("Mesquita", 1, 200)
    g = Gerente(senha = 12345667, qtd_funcionarios = 3, nome = "Tista", nif = 1, salario = 3000)
    print(f.nome)
    print(g.nome)
    
