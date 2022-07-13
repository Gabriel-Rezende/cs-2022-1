
if __name__ == '__main__':
    vetor = [None] * 10

    cont = 0
    valor = None
    while valor != 0:
        try:
            valor = int(input("Digite um número: "))
        except ValueError as ve:
            print(ve)

        try:
            vetor[cont] = valor
            cont += 1
        except IndexError as ie:
            if valor == 0:
                vetor[-1] = valor
            print(ie)

    print(vetor)
