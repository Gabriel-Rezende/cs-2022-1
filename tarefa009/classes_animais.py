
class Animal:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        return 'som'

class Cachorro(Animal):

    def emitir_som(self):
        return "Som do cachorro"

    def correr(self):
        return "Correndo"


class Cavalo(Animal):

    def emitir_som(self):
        return "Som do cavalo"

    def correr(self):
        return "Correndo"


class Preguica(Animal):

    def emitir_som(self):
        return "Som da preguiça"
    
    def subir_arvore(self):
        return "Subindo em árvores"


class Veterinario():

    def examinar(self, animal):
        print(animal.emitir_som())
        

class Zoologico():
    
    def __init__(self):
        self.jaulas = list()