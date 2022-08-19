
"""Se o atributo taxa_mensal ficasse na ContaBancaria ele seria opcional, dado que contas poupanças não tem taxa mensal
Logo, foram criadas 2 subclasses com uma contendo a taxa mensal e outra não."""


class ContaBancaria:

    def __int__(self, agencia, conta, cdg_verificador):
        self.agencia = agencia
        self.conta = conta
        self.cdg_verificador = cdg_verificador


class ContaCorrente:

    def __int__(self, agencia, conta, cdg_verificador, taxa_mensal):
        super().__init__(agencia, conta, cdg_verificador)
        self.taxa_mensal = taxa_mensal


class ContaPoupanca:

    def __int__(self):
        pass
