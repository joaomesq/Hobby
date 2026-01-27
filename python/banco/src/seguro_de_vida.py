from tributavel_mix_in import TributavelMixIn

class SeguroDeVida(TributavelMixIn):

    __slots__ = ['_valor', '_titular', '_numero_apolice']
    
    def __init__(self, valor, titular, numero_apolice):
        self._titular = titular
        self._valor = valor
        self._numero_apolice = numero_apolice

    def get_valor_imposto(self):
        return 50 + self._valor * 0.05