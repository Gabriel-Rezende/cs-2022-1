
def divisao(dividendo, divisor):
    return dividendo / divisor

if __name__ == '__main__':
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        try:
            resultado = divisao(num1, num2)
            print(f"Resultado da Divisão: {resultado}")
        except ArithmeticError as ae:
            print(ae)
    except ValueError as ve:
        print(ve)