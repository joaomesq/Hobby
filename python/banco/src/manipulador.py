class ManipuladorTributaveis:
    def calcular_impostos(self, lista_tributaveis):
        total = 0
        for t in lista_tributaveis:
            total += t.get_valor_imposto()
        
        return total


if __name__ == "__main__":
    from  conta import ContaCorrente
    from seguro_de_vida import SeguroDeVida

    c1 = ContaCorrente(saldo = 1000, numero = 1, titular = "Mesquita" )
    c2 = ContaCorrente(saldo = 200, numero = 2, titular = "Euclides")
    seguro = SeguroDeVida(valor = 100, titular = "Augusto", numero_apolice = 1)

    lt = []
    lt.append(c1)
    lt.append(c2)
    lt.append(seguro)

    print(c1.get_valor_imposto())
    print(c2.get_valor_imposto())
    print(seguro.get_valor_imposto())

    manipulador = ManipuladorTributaveis()
    print(manipulador.calcular_impostos(lt))