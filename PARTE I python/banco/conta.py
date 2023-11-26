from abc import ABC, abstractclassmethod


class Conta(ABC):
    """
    Classe abstrata que representa uma conta genérica em um sistema bancário.

    Attributes:
        agencia (str): O número da agência da conta.
        conta (str): O número da conta.
        saldo (float): O saldo atual da conta.

    Methods:
        depositar(valor: float) -> None:
            Realiza um depósito na conta.

        detalhes() -> None:
            Exibe os detalhes da conta, incluindo agência, número da conta e saldo.

        sacar(valor: float) -> None:
            Método abstrato para realizar um saque na conta. Deve ser implementado nas subclasses.
    """

    def __init__(self, agencia, conta, saldo):
        """
        Inicializa uma nova instância da classe Conta.

        Args:
            agencia (str): O número da agência da conta.
            conta (str): O número da conta.
            saldo (float): O saldo inicial da conta.
        """
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        """
        Getter para o número da agência da conta.

        Returns:
            str: O número da agência da conta.
        """
        return self._agencia

    @property
    def conta(self):
        """
        Getter para o número da conta.

        Returns:
            str: O número da conta.
        """
        return self._conta

    @property
    def saldo(self):
        """
        Getter para o saldo da conta.

        Returns:
            float: O saldo atual da conta.
        """
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        """
        Setter para o saldo da conta.

        Args:
            valor (float): O novo valor do saldo.

        Raises:
            ValueError: Se o valor fornecido não for um número.
        """
        if not isinstance(valor, (int, float)):
            raise ValueError("O saldo precisa ser um número")
        self._saldo = valor

    def depositar(self, valor):
        """
        Realiza um depósito na conta.

        Args:
            valor (float): O valor a ser depositado na conta.

        Raises:
            ValueError: Se o valor do depósito não for um número.
        """
        if not isinstance(valor, (int, float)):
            raise ValueError("O valor do depósito precisa ser um número")

        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        """
        Exibe os detalhes da conta, incluindo agência, número da conta e saldo.
        """
        print(f"Agência: {self.agencia}", end='')
        print('____' * 5, '___' * 5)

        print(f"Conta: {self.conta}", end='')
        print('____' * 5, '___' * 5)

        print(f"Saldo: {self.saldo}", end='')

    @abstractclassmethod
    def sacar(self, valor):
        """
        Método abstrato para realizar um saque na conta. Deve ser implementado nas subclasses.

        Args:
            valor (float): O valor a ser sacado da conta.
        """
        pass


        