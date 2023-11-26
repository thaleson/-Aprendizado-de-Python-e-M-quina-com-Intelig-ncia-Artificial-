from conta import Conta


class ContaCorrente(Conta):
    """
    Classe que representa uma conta corrente, derivada da classe Conta.

    Attributes:
        agencia (str): O número da agência da conta.
        conta (str): O número da conta.
        saldo (float): O saldo atual da conta corrente.
        limite (float): O limite de crédito associado à conta corrente.

    Methods:
        sacar(valor: float) -> None:
            Realiza um saque na conta corrente, considerando o limite de crédito.

    """

    def __init__(self, agencia, conta, saldo, limite=100):
        """
        Inicializa uma nova instância da classe ContaCorrente.

        Args:
            agencia (str): O número da agência da conta.
            conta (str): O número da conta.
            saldo (float): O saldo inicial da conta corrente.
            limite (float, optional): O limite de crédito associado à conta corrente. Padrão é 100.
        """
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        """
        Getter para o limite de crédito da conta corrente.

        Returns:
            float: O limite de crédito associado à conta corrente.
        """
        return self._limite

    def sacar(self, valor):
        """
        Realiza um saque na conta corrente, considerando o limite de crédito.

        Args:
            valor (float): O valor a ser sacado da conta corrente.

        Raises:
            ValueError: Se o valor do saque não for um número.

        """
        if not isinstance(valor, (int, float)):
            raise ValueError("O valor do saque precisa ser um número")

        if self.saldo + self.limite < valor:
            print("Saldo insuficiente")
            return

        self.saldo -= valor
        self.detalhes()
