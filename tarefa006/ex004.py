

if __name__ == '__main__':
    ipi = float(input('Digite a porcentagem de IPI: '))
    cod_peca1 = input('Digite o código da peça 1: ')
    valor_peca1 = float(input('Digite o valor unitário da peça 1: '))
    qtd_peca1 = int(input('Digite a quantidade de peças 1: '))

    cod_peca2 = input('Digite o código da peça 2: ')
    valor_peca2 = float(input('Digite o valor unitário da peça 2: '))
    qtd_peca2 = int(input('Digite a quantidade de peças 2: '))

    valor_total = ((valor_peca1 * qtd_peca1) + (valor_peca2 * qtd_peca2)) * (ipi/100 + 1)
    print(f'Valor total: R$ {valor_total}')