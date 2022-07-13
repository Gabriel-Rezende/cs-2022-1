

class LoginInvalidoException(Exception):
    pass


class Login:

    def __init__(self, usuario, senha):
        self.usuario = usuario
        self.senha = senha

    def fazer_login(self, usuario, senha):
        if self.usuario == usuario and self.senha == senha:
            return True
        else:
            raise LoginInvalidoException("Login Inválido")

if __name__ == '__main__':
    login = Login('gabriel.pires', 'teste')
    try:
        login.fazer_login('obadias', 'obedes')
    except LoginInvalidoException as lie:
        print(lie)