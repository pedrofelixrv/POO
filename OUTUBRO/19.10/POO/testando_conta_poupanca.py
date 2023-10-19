from conta_poupanca import ContaPoupanca
from conta import Conta

class CriarPoupanca:
    if __name__ == '__main__':

        conta = Conta("21.342-7")
        print(type(conta))
        conta = ContaPoupanca("21.342-7")
        print(type(conta))

        conta.creditar(500.87)
        conta.debitar(45.00)
        print(conta.get_saldo())
