from conta import Conta
from contaespecial import ContaEspecial

conta = Conta("31.345-X")
conta.creditar(20)
especial = ContaEspecial("31.567-x")
conta.creditar(20)
conta = especial
conta.creditar(20)