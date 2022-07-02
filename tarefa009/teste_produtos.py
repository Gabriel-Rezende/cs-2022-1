from classes_produtos import *

class ProdutoTeste():

    def __init__(self, carrinho):
        self.carrinho = carrinho

if __name__ == '__main__':
    mouse1 = Mouse("Loja 1", 50.00, "Mouse bonito1", "tipo do mouse1")
    mouse2 = Mouse("Loja 1", 60.00, "Mouse bonito2", "tipo do mouse2")
    mouse3 = Mouse("Loja 1", 70.00, "Mouse bonito3", "tipo do mouse3")
    mouse4 = Mouse("Loja 1", 80.00, "Mouse bonito4", "tipo do mouse4")
    mouse5 = Mouse("Loja 1", 90.00, "Mouse bonito5", "tipo do mouse5")
    mouse6 = Mouse("Loja 1", 100.00, "Mouse bonito6", "tipo do mouse6")
    livro1 = Mouse("Loja 1", 110.00, "Livro legal1", "Autor do livro1")
    livro2 = Mouse("Loja 1", 120.00, "Livro legal2", "Autor do livro2")
    livro3 = Mouse("Loja 1", 130.00, "Livro legal3", "Autor do livro3")
    livro4 = Mouse("Loja 1", 140.00, "Livro legal4", "Autor do livro4")
    produto_teste = ProdutoTeste(list([mouse1, mouse2, mouse3, mouse4, mouse5, mouse6, livro1, livro2, livro3, livro4]))

    for item in produto_teste.carrinho:
        print(item.get_descricao())