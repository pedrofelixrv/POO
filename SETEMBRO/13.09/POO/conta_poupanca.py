from conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, numero):
        super().__init__(numero)

    def __int__(self, taxa):
        self.creditar(self.get_saldo()*taxa)
