import abc

class Autenticavel(abc.ABC):
    """
    Esta classe serve de interface para objectos autenticavel

    As subclasse devem sobreescrever o método autentica
    """

    @abc.abstractmethod
    def autentica(self, senha):
        """
        Método abstracto que faz a verificação da senha
        Retorna True se for igual/válida, Retorna False caso contrário
        :param self: Description
        """
        pass