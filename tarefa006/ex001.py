
def idade_em_dias(anos, meses, dias):
    total_dias = (anos * 365) + (meses * 30) + dias
    return total_dias



if __name__ == '__main__':
    anos = int(input('Digite quantos anos você tem: '))
    meses = int(input('Digite quantos meses: '))
    dias = int(input('Digite quantos dias: '))
    print(idade_em_dias(anos, meses, dias))
