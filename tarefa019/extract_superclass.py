
# Antes de refatorar, Funcionario e Gerente teriam repetidamente os atributos da superclasse

class PessoaSuper:

    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo


class Funcionario(PessoaSuper):

    def __init__(self, nome, idade, sexo, salario):
        super().__init__(nome, idade, sexo)
        self.salario = salario


class Gerente(PessoaSuper):

    def __init__(self, nome, idade, sexo, comissao):
        super().__init__(nome, idade, sexo)
        self.comissao = comissao
