import re


def validar_login(usuario):
    if re.match('^.{5,30}$', usuario):
        return True
    else:
        return False


def validar_senha(senha):
    if re.match('(?=.*\d)(?=.*[A-Z])(?=.*\W)(?=^.{8,12}$)', senha):
        return True
    else:
        return False


if __name__ == '__main__':
    print(validar_login('aaaaaA2#aaa'))
    print(validar_senha('Testando123@'))
