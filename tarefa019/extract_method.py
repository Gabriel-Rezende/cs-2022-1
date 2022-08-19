
def somar_em_numero_e_imprimir(numero, valor_a_somar):
    numero += valor_a_somar
    imprimir_numero(numero)  # Extraído em um método


def imprimir_numero(numero):
    print('O valor do número é: ', numero)
