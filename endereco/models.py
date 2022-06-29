from enum import Enum
from abc import ABC, abstractmethod


class IEndereco(ABC):

    @abstractmethod
    def consulta_por_cep(self, cep):


class IEnderecoImpl(IEndereco):

    def consulta_por_cep(self, cep):
        return None


class Pais():

    def __init__(self, nome):
        self.nome = nome


class Estado():

    def __init__(self, sigla, nome, pais)
        self.__sigla = sigla
        self.nome = nome
        self.pais = pais


class Cidade():

    def __init__(self, nome, estado):
        self.__nome = nome
        self.estado = estado


class Bairro():

    def __init__(self, nome, cidade):
        self.__nome = nome
        self.cidade = cidade


class Endereco():

    def __init__(self, numero, complemento, cep, bairro, logradouro, tipo_endereco):
        self.__numero = numero
        self.__complemento = complemento
        self.__cep = cep
        self.bairro = bairro
        self.logradouro = logradouro
        self.tipo_endereco = tipo_endereco


class TipoEndereco(Enum)
    COMERCIAL = 1
    RESIDENCIAL = 2


class Logradouro():

    def __init__(self, nome, tipo_logradouro):
        self.__nome = nome
        self.tipo_logradouro = tipo_logradouro


class TipoLogradouro(Enum)
    ALAMEDA = 1
    AVENIDA = 2
    MARGINAL = 3
    RUA = 4
    RODOVIA = 5
    VIA = 6
    VIELA = 7
    TRAVESSA = 8


class PessoaFisica():

    def __init__(self, nome, sexo, data_nascimento, endereco):
        self.__nome = nome
        self.__sexo = sexo
        self.__data_nascimento = data_nascimento
        self.endereco = endereco
