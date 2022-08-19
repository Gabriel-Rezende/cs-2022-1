from encapsulate_field import PessoaEncapsulada, Pessoa
from extract_method import somar_em_numero_e_imprimir
from extract_class import Cliente, Telefone
from extract_superclass import Funcionario, Gerente, PessoaSuper

if __name__ == '__main__':
    # Encapsulate Field
    p1 = Pessoa('Gabriel', 13)
    print(p1.idade)

    p2 = PessoaEncapsulada('Gabriela', 15)
    print(p2.get_idade())  # p2.idade ou p2.__idade não retornaria o dado por ser privado

    # Extract Method
    somar_em_numero_e_imprimir(10, 5)

    # Extract Class
    c1 = Cliente('Jean', 15, Telefone('62', '98765-4321'))
    print(c1.telefone)

    # Extract Superclass
    f1 = Funcionario('Maria', 30, 'F', 5000)
    g1 = Gerente('Maria', 30, 'F', 0.1)
    print(isinstance(f1, PessoaSuper))
    print(isinstance(g1, PessoaSuper))
