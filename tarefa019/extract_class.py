
class Cliente:

    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone  # Extraído em uma classe própria


class Telefone:

    def __init__(self, ddd, numero):
        self.ddd = ddd
        self.numero = numero

    def __str__(self):
        return f'({self.ddd}) {self.numero}'
