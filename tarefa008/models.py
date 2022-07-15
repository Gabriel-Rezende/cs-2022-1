from enum import Enum
from abc import ABC, abstractmethod


class IEndereco(ABC):

    @abstractmethod
    def consulta_por_cep(self, cep):
        """Método para consulta de Endereço através do CEP

        Args:
            cep (string): CEP a ser consultado
        """
        pass

class IEnderecoImpl(IEndereco):

    def consulta_por_cep(self, cep):
        """Método para consulta de Endereço através do CEP

        Args:
            cep (string): CEP a ser consultado
        """
        return None


class Pais():
    """Classe País"""
    
    def __init__(self, nome):
        """Construtor da classe País

        Args:
            nome (string): nome do país
        """
        self.nome = nome


class Estado():
    """Classe Estado"""

    def __init__(self, sigla, nome, pais):
        """Construtor da classe Estado

        Args:
            sigla (string): sigla do estado
            nome (string): nome do estado
            pais (Pais): país do estado
        """
        self.__sigla = sigla
        self.nome = nome
        self.pais = pais


class Cidade():
    """Classe Cidade"""

    def __init__(self, nome, estado):
        """Construtor da classe Cidade

        Args:
            nome (string): nome da cidade
            estado (Estado): estado da cidade
        """
        self.__nome = nome
        self.estado = estado


class Bairro():
    """Classe Bairro"""
    
    def __init__(self, nome, cidade):
        """Construtor da classe Bairro

        Args:
            nome (string): nome do bairro
            cidade (Cidade): cidade do bairro
        """
        self.__nome = nome
        self.cidade = cidade


class Endereco():
    """Classe que representa um Endereço"""

    def __init__(self, numero, complemento, cep, bairro, logradouro, tipo_endereco):
        """Construtor da classe Endereço

        Args:
            numero (int): numero do endereço
            complemento (string): complemento do endereço
            cep (string): cep do endereço
            bairro (string): bairro do endereço
            logradouro (Logradouro): logradouro do endereço
            tipo_endereco (TipoEndereco): tipo do endereço
        """
        self.__numero = numero
        self.__complemento = complemento
        self.__cep = cep
        self.bairro = bairro
        self.logradouro = logradouro
        self.tipo_endereco = tipo_endereco


class TipoEndereco(Enum):
    """Enum de tipo de endereço"""
    COMERCIAL = 1
    RESIDENCIAL = 2


class Logradouro():
    """Classe que representa um logradouro"""

    def __init__(self, nome, tipo_logradouro):
        """Construtor da classe Logradouro

        Args:
            nome (string): nome do logradouro
            tipo_logradouro (TipoLogradouro): tipo do logradouro
        """
        self.__nome = nome
        self.tipo_logradouro = tipo_logradouro


class TipoLogradouro(Enum):
    """Enum com as opções de tipos de logradouro"""

    ALAMEDA = 1
    AVENIDA = 2
    MARGINAL = 3
    RUA = 4
    RODOVIA = 5
    VIA = 6
    VIELA = 7
    TRAVESSA = 8


class PessoaFisica():
    """Classe para representar uma Pessoa Física"""

    def __init__(self, nome, sexo, data_nascimento, endereco):
        """Construtor de Pessoa Física

        Args:
            nome (string): nome da pessoa
            sexo (char): sexo da pessoa
            data_nascimento (string): Data de nascimento da pessoa física
            endereco (Endereco): Endereço da pessoa
        """
        self.__nome = nome
        self.__sexo = sexo
        self.__data_nascimento = data_nascimento
        self.endereco = endereco
