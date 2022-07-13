

class SaldoInsuficienteException(Exception):
    pass


class ContaBancaria:

    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            raise SaldoInsuficienteException("Saldo Insuficiente")
        else:
            self.saldo -= valor


if __name__ == '__main__':
    cb = ContaBancaria(500)
    cb.depositar(700)
    try:
        cb.sacar(1300)
    except SaldoInsuficienteException as sie:
        print(sie)