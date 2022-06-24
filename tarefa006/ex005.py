
def calcula_salarios_minimos(salario_total, salario_minimo):
    return salario_total / salario_minimo

if __name__ == '__main__':
    salario_minimo = float(input('Digite o valor do salário mínimo: '))
    salario_total = float(input('Digite o valor do salário a ser calculado: '))
    qtd_salarios = calcula_salarios_minimos(salario_total, salario_minimo)
    print(f'Esse salário é {qtd_salarios} vezes um salário mínimo.')