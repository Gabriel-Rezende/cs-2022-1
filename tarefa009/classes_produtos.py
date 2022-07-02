
class Produto():
    
    def __init__(self, nomeloja, preco):
        self.nomeloja = nomeloja
        self.preco = preco
        self.descricao = "Produto de informática"

    def get_descricao(self):
        return self.descricao

class Mouse(Produto):

    def __init__(self, nomeloja, preco, descricao, tipo):
        super().__init__(nomeloja, preco)
        self.descricao = descricao
        self.tipo = tipo

    def get_descricao(self):
        return f'{self.descricao} - {self.tipo}'

class Livro(Produto):

    def __init__(self, nomeloja, preco, descricao, autor):
        super().__init__(nomeloja, preco)
        self.descricao = descricao
        self.autor = autor

    def get_descricao(self):
        return f'{self.descricao} - {self.autor}'