from closures import make_multiplier_of
from generics import first
from typing import List
from logging_custom import create_warning_log

if __name__ == '__main__':
    # Closure
    # Cria uma "instância" do método make_multiplier_of com o valor 3, depois outra instância com o valor 5
    times3 = make_multiplier_of(3)
    print(times3(5))

    times5 = make_multiplier_of(5)
    print(times5(10))

    # Generics
    list_one: List[str] = ["a", "b", "c"]
    print(first(list_one))

    list_two: List[int] = [1, 2, 3]
    print(first(list_two))

    # Logging
    create_warning_log('AVISO! Você foi avisado.')


