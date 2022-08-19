
# Versão não encapsulada
class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


# Versão encapsulada
class PessoaEncapsulada:

    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade
