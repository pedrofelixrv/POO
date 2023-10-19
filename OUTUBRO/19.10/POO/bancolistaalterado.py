
"class BancoLista:

    'def debitar(self, numero, valor):
        'conta = self.procurar_conta(numero)
        'if conta:
            'if conta.get_saldo() >= valor:
                'conta.debitar(valor)
            'else:
                'raise SIException(conta.get_saldo(), conta.get_numero())
        'else:
            'raise CIException(numero)